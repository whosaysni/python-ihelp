# coding: utf-8
# Copyright (c) 2010, 2011 Yasushi Masuda. All rights reserved.
"""
python-ihelp: i18n version of help().

Language pack name format: ihelp_<language>__<package_name>

"""
import hashlib, inspect, locale, operator, os, pydoc, re, sys, warnings


class IHelpWarning(Warning):
    """Warning generated in ihelp.
    """
    pass

warnings.filterwarnings('once', category=IHelpWarning)


class GetDoc(object):
    """i18n-integrated GetDoc.
    """
    def __init__(self, language=(locale.getlocale()[0]
                                 or locale.getdefaultlocale()[0]),
                 ignore_cache=False, _getdoc=None):
        """Initializer.
        """
        self.language = language
        # if ignore_cache is True, disable cache mechanism.
        if ignore_cache:
            self.cache = None
        else:
            self.cache = {}
        # self._getdoc defaults to pydoc.getdoc.
        if _getdoc is None:
            import pydoc
            _getdoc = pydoc.getdoc
        self._getdoc = _getdoc
        # load special (builtin) bundle.
        if not (self.cache is None):
            self.cache.update(self.load_catalog_bundle('this', language))

    def load_catalog(self, package_name, language=None):
        """Loads a catalog corresponding to package_name.
        """
        if language is None:
            language = str(self.language)
        key_tuple = (package_name, language)
        # simply return if catalog is already loaded.
        if self.cache and key_tuple in self.cache.keys():
            return self.cache[key_tuple]
        # ... else, try to load catalog.
        catalog_modname = 'ihelp_%s__%s' %(language, package_name)
        try:
            catalog_module = __import__(catalog_modname)
        except ImportError:
            sys.stderr.write('Warning: unable to load catalog module: %s\n'
                             %(catalog_modname))
            catalog_module = None
        # if catalog_module is valid, put it to cache.
        if catalog_module:
            if hasattr(catalog_module, 'ihelp'):
                catalog = catalog_module.ihelp
                if self.cache is not None:
                    self.cache[(package_name, language)] = catalog
            else:
                sys.stderr.write('Warning: no ihelp in catalog: %s.\n'
                                 %(catalog_modname))
                catalog = {}
        else:
            catalog = {}
        return catalog

    def load_catalog_bundle(self, bundle_name, language):
        """Loads bundle-type catalog.
        """
        if language is None:
            language = str(self.language)
        # try to load bundle.
        bundle_modname = 'ihelpbundle_%s__%s' %(language, bundle_name)
        try:
            bundle_module = __import__(bundle_modname)
        except ImportError:
            sys.stderr.write('Warning: unable to load catalog bundle module: %s\n'
                             %(bundle_modname))
            bundle_module = None
        # if bundle_module is valid, load bundled catalog.
        bundled_catalogs = {}
        if bundle_module:
            if hasattr(bundle_module, 'package_names'):
                package_names = bundle_module.package_names
            else:
                sys.stderr.write('Warning: could not find package_names in bundle: %s.\n'
                                 %(bundle_modname))
                package_names = []
            for package_name in package_names:
                catalog_modname = bundle_modname+'.'+package_name
                try:
                    catalog_module = getattr(__import__(catalog_modname),
                                             package_name, None)
                except ImportError:
                    sys.stderr.write('Warning: unable to load catalog module: %s\n'
                                     %(catalog_modname))
                    catalog_module = None
                if catalog_module:
                    if hasattr(catalog_module, 'ihelp'):
                        catalog = catalog_module.ihelp
                        bundled_catalogs[(package_name, language)] = catalog
                    else:
                        sys.stderr.write('Warning: no ihelp in catalog module: %s\n'
                                         %(catalog_modname))
        return bundled_catalogs

    def resolve_object_path(self, obj):
        """Determines package and name for given object.
        """
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
            # "<__objclass__ module name>.<__objclass__ name>.<method name>".
            if hasattr(obj, '__name__'):
                # if obj has its own __name__
                # look for __doc__ in base classes
                for cls in reversed(getattr(obj.__objclass__, '__bases__', [])):
                    if (hasattr(cls, obj.__name__) and
                        hasattr(getattr(cls, obj.__name__), '__doc__') and
                        getattr(cls, obj.__name__).__doc__==self._getdoc(obj)):
                        module_path_bits = (
                            str(inspect.getmodule(cls).__name__).split('.')+
                            cls.__name__.split('.'))
                        object_name = '.'.join(module_path_bits[1:]+[obj.__name__])
            # else, derive names from obj.__objclass__
            else:
                module_path_bits = (
                    str(inspect.getmodule(obj.__objclass__).__name__).split('.')+
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

    def get_translation(self, package_name, object_name, doc, language=None):
        catalog = self.load_catalog(package_name, language)
        # now we have the catalog, try to translate.
        if object_name in catalog:
            last_valid = None
            doc_signature = hashlib.md5(doc).hexdigest()
            for signature, valid, translated in catalog[object_name]:
                # translation should be valid and...
                if valid:
                    last_valid = translated
                    # ... its signature should match.
                    if signature==doc_signature:
                        doc = last_valid
                        break
            # if no signatures match, use last valid translation.
            else:
                if last_valid:
                    # signature is diffrent to the catalog. Issues warning.
                    doc = last_valid
                    sys.stderr.write(
                        'Warning: translated docstring found in ihelp '
                        'catalog, but it is for different version of '
                        'module. Showing it anyway...\n')
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


def shadow_module(module_name, shadow_name):
    """Shadows a module with given shadow_name.
    """
    import imp, sys
    # always purges existing module under the shadow_name
    if shadow_name in sys.modules:
        sys.modules.pop(shadow_name)
    return imp.load_module(shadow_name, *imp.find_module(module_name))


def install(*args, **kwargs):
    """Installs ihelp.
    """
    _ipydoc = shadow_module('pydoc', '_ipydoc')
    _ipydoc.getdoc = GetDoc(*args, **kwargs).getdoc
    # installs ihelp under __builtin__ namespace.
    import __builtin__
    __builtin__.ihelp = _ipydoc.Helper(sys.stdin, sys.stdout)
    del __builtin__

install()
