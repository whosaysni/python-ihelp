import hashlib, inspect, locale, logging, operator, os, pydoc, re, sys, warnings


class DocstringTranslationObsoleted(Warning):
    pass
warnings.filterwarnings('once', category=DocstringTranslationObsoleted)

# language pack name format: ihelp_ja_JP__pkgname

class GetDoc(object):
    
    @classmethod
    def _reset_ihelp_docs(cls):
        cls.ihelp_docs = {}

    def _load_ihelp_docs(cls, language):
        prefix = 'ihelp_'+language
        for module_name in sys.modules.keys():
            module = __import__(module_name)
            cls.ihelp_docs.update(getattr(module, 'ihelp', {}))
    
    def __init__(self, language=(locale.getlocale()[0]
                                 or locale.getdefaultlocale()[0]),
                 ignore_cache=False, _getdoc=None):
        """Initializer.
        """
        self.language = language
        if ignore_cache:
            self.cache = None
        else:
            self.cache = {}
        if _getdoc is None:
            import pydoc
            _getdoc = pydoc.getdoc
        self._getdoc = _getdoc

    def load_catalog(self, package_name, language=None):
        """Load a catalog corresponding to package_name
        """
        if language is None:
            language = str(self.language)
        key_tuple = (package_name, language)
        # simply return if catalog is already loaded.
        if self.cache and key_tuple in self.cache.keys():
            return self.cache[key_tuple]
        # ... else try to load catalog.
        catalog_modname = 'ihelp_%s__%s' %(package_name, language)
        try:
            catalog_module = __import__(catalog_modname)
        except ImportError:
            warnings.warn(u'Unable to load catalog module: %s' %(catalog_modname))
            catalog_module = None
        if catalog_module:
            catalog = catalog_module.ihelp
            if self.cache is not None:
                self.cache[(package_name, language)] = catalog
        else:
            catalog = {}
        return catalog

    def resolve_object_path(self, obj):
        module_path_bits, object_name = [], None
        if inspect.ismethoddescriptor(obj):
            # avoid failing getmodule for method descriptors
            mod = None
        else:
            mod = inspect.getmodule(obj)
        if mod is not None:
            # non-null module should have ordinal module path.
            module_path_bits = str(mod.__name__).split('.')
        elif hasattr(obj, '__objclass__'):
            # those methods having __objclass__ can be specified as
            # "<__objclass__'s module>.<__objclass__'s name>.<method name>".
            if hasattr(obj, '__name__'):
                # look __doc__ for base classes
                for cls in reversed(getattr(obj.__objclass__, '__bases__', [])):
                    if (hasattr(cls, obj.__name__) and
                        hasattr(getattr(cls, obj.__name__), '__doc__') and
                        getattr(cls, obj.__name__).__doc__==self._getdoc(obj)):
                        module_path_bits = (
                            str(inspect.getmodule(cls).__name__).split('.')+
                            cls.__name__.split('.'))
                        object_name = '.'.join(module_path_bits[1:]+[obj.__name__])
            if not module_path_bits:
                module_path_bits = (
                    str(inspect.getmodule(obj.__objclass__).__name__).split('.') +
                    obj.__objclass__.__name__.split('.'))
        elif hasattr(obj, 'im_class'):
            # not sure if this path is used... Just for completeness.
            # "<im_class's module>.<im_class' name>".
            module_path_bits = (
                str(inspect.getmodule(obj.im_class).__name__).split('.'))
        elif obj in vars(operator).values():
            # for builtin operators, use "__builtin__.object.<method name>".
            module_path_bits = ['__builtin__', 'object']
        else:
            # here, just give up understanding slithy internals.
            module_path_bits = ['__undefined__']
        package_name = module_path_bits[0] if module_path_bits else ''
        if object_name is None:
            object_name = '.'.join(module_path_bits[1:] + [obj.__name__])
        return package_name, object_name

    def get_signature(self, doc):
        return hashlib.md5(doc).hexdigest()

    def get_translation(self, package_name, object_name, doc, language=None):
        catalog = self.load_catalog(package_name, language)
        # now we have the catalog, try to translate.
        if catalog:
            if object_name in catalog:
                last_valid = None
                for signature, valid, translated in catalog[object_name]:
                    # translation should be valid and...
                    if valid:
                        last_valid = translated
                        # ... its signature should match.
                        if signature==self.get_signature(doc):
                            doc = translated
                            break
                # if no signatures match, use last valid translation.
                if last_valid:
                    # signature is diffrent to the catalog. Warning required.
                    doc = last_valid
                    warning.warn('Translated docstring found in ihelp catalog, '
                                 'but it is for different version of module. '
                                 'Showing it anyway...', category=DocstringTranslationObsoleted)
        return doc

    def getdoc(self, obj, language=None):
        """Get the doc string or comments for an object."""
        # get original document.
        doc = self._getdoc(obj)
        # build unique path for object.
        package_name, object_name = self.resolve_object_path(obj)
        # look catalog for package_name and language.
        idoc = self.get_translation(package_name, object_name, doc, language)
        # strips leading blank line
        if idoc:
            idoc = re.sub('^ *\n', '', idoc.rstrip())
        else:
            idoc = ''
        return idoc


class DocDistiller(GetDoc):

    def __init__(self, *args, **kwargs):
        super(DocDistiller, self).__init__(*args, **kwargs)
        self.updated_packages = []

    def escape_document(self, doc):
        return (doc.replace("\\", "\\\\")
                .replace('"', r'\"')
                .replace("'", r'\"'))

    def dump_catalog(self, package_name, catalog):
        catalog_fn = self.get_catalog_filename(package_name)
        catalog_file = open(catalog_fn, 'wb')
        catalog_file.write('{\n')
        for object_name in sorted(catalog.keys()):
            catalog_file.write("'%s': [\n" %(object_name))
            for signature, valid, doc in catalog[object_name]:
                catalog_file.write("('%s', %s, \n\"\"\"" %(signature, valid))
                catalog_file.write(self.escape_document(doc))
                catalog_file.write("\"\"\"),\n\n")
            catalog_file.write("],\n\n\n")
        catalog_file.write('}\n')
        catalog_file.close()
    
    def getdoc(self, obj):
        # get original document.
        doc = self._getdoc(obj)
        # first, build unique path for object.
        package_name, object_name = self.resolve_object_path(obj)
        # second, get the catalog
        catalog = self.get_catalog(package_name)
        updated = False
        if object_name not in catalog:
            updated = True
            catalog[object_name] = []
        entries = catalog[object_name]
        signature = self.get_signature(doc)
        if signature not in (e[0] for e in entries):
            updated = True
            catalog[object_name].append((signature, False, doc))
        if updated:
            self.updated_packages.append(package_name)

    def dump_docs(self):
        for package_name in self.updated_packages:
            catalog = self.cache.get(package_name, None)
            if catalog is not None:
                self.dump_catalog(package_name, catalog)


def shadow_module(module_name, shadow_name):
    """Shadows a module with given shadow_name.
    """
    import imp, sys
    # always purges existing module under the shadow_name
    if module_name in sys.modules:
        sys.modules.pop(module_name)
    return imp.load_module(module_name, *imp.find_module(base_module_name))


def dump_catalog(module_names, *args, **kwargs):
    """Dumps catalog.
    """
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO
    # initialize docstring distiller.
    distiller = DocDistiller(*args, **kwargs)
    # set up shadowed module.
    shadow_name = '_ipydoc_dump'
    shadowed_module = shadow_module('pydoc', shadow_name)
    shadowed_module.getdoc = distiller.getdoc
    help = shadowed_module.Helper(StringIO(), StringIO())
    # queue docstrings into overriden getdoc().
    for module_name in module_names:
        help(module_name)
    # distill and dump.
    distiller.dump_docs()
    # teardown, purging shadowed module.
    del shadowed_module
    sys.modules.pop(shadow_name)


def install(*args, **kwargs):
    """Installs ihelp.
    """
    _ipydoc = shadow_module('pydoc', '_ipydoc')
    _ipydoc.getdoc = GetDoc(*args, **kwargs).getdoc
    # installs ihelp under __builtin__ namespace.
    import __builtin__
    __builtin__.ihelp = _ipydoc.Helper(sys.stdin, sys.stdout)
    del __builtin__

# install()
