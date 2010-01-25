import hashlib, inspect, locale, logging, operator, os, pydoc, re, sys, warnings

# At default, ihelp files are located under ~/.ihelp.
PY_IHELP_ROOT = os.path.join(os.path.expanduser('~'), '.ihelp')


class GetDoc(object):
    def __init__(self,
                 language=(locale.getlocale()[0]
                           or locale.getdefaultlocale()[0]),
                 ignore_cache=False, _getdoc=None):
        """Initializer.
        """
        self.language = language
        self.cache = None if ignore_cache else {}
        if _getdoc is None:
            import pydoc
            _getdoc = pydoc.getdoc
        self._getdoc = _getdoc

    def get_catalog_filename(self, package_name):
        return os.path.join(
            PY_IHELP_ROOT, '%s.%s.ihelp' %(package_name, self.language))

    def load_catalog(self, package_name):
        """Load a catalog corresponding to package_name
        """
        catalog_fn = self.get_catalog_filename(package_name)
        catalog = {}
        if os.path.exists(catalog_fn):
            try:
                catalog = eval(
                    unicode(open(catalog_fn, 'rb').read(), 'utf-8', 'ignore'),
                    dict(__builtins__=None, True=True, False=False), None)
            except:
                warnings.warn(u'Unable to load catalog: %s' %(catalog_fn))
                catalog = {}
        else:
            catalog = {}
        # store loaded catalog to cache, if enabled.
        if self.cache is not None:
            self.cache[package_name] = catalog
        return catalog

    def get_catalog(self, package_name):
        """Get a catalog, using cache if enabled.
        """
        if self.cache is None:
            catalog = self.load_catalog(package_name)
        else:
            if package_name not in self.cache:
                self.cache[package_name] = self.load_catalog(package_name)
            catalog = self.cache[package_name]
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

    def get_translation(self, package_name, object_name, doc):
        # now we have the catalog, try translation.
        catalog = self.get_catalog(package_name)
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
                    doc = last_valid
                    # TBD: The document may be obsolete here --
                    # signature is diffrent to the catalog. Notification required.
        return doc

    def getdoc(self, obj):
        """Get the doc string or comments for an object."""
        # get original document.
        doc = self._getdoc(obj)
        # first, build unique path for object.
        package_name, object_name = self.resolve_object_path(obj)
        # second, lookup catalog for package_name and language.
        doc = self.get_translation(package_name, object_name, doc)
        return re.sub('^ *\n', '', doc.rstrip()) if doc else ''


class CatalogGetDoc(GetDoc):

    def escape_doument(self, doc):
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
            catalog_file.write("],\n\n\n" %(object_name))
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
            self.dump_catalog(package_name, catalog)


def install(*args):
    import __builtin__, imp, sys
    if '_ipydoc' in sys.modules:
        sys.modules.pop('_ipydoc')
    _ipydoc = imp.load_module('_ipydoc', *imp.find_module('pydoc'))
    _ipydoc.getdoc =  GetDoc(*args).getdoc
    __builtin__.ihelp = _ipydoc.Helper(sys.stdin, sys.stdout)
    del imp, __builtin__


install()
