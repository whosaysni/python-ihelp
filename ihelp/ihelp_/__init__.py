# coding: utf-8
# Copyright (c) 2010, 2011 Yasushi Masuda. All rights reserved.
"""
python-ihelp: i18n version of help().

Language pack name format: ihelp_<language>__<package_name>

"""
import __builtin__
import hashlib, inspect, locale, logging, operator, os, re, sys, warnings


# logger settings
DEBUG = False
_logger = None
def _debug(*args):
    """Internal debug function.
    """
    if DEBUG==False:
        return
    global _logger
    if _logger is None:
        import logging
        _logger = logging.getLogger('ihelp')
    return _logger.debug(*args)

# exception
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
        _debug("GetDoc(language='%s', ignore_cache=%s, _getdoc=%s)",
               language, ignore_cache, _getdoc)

    def load_catalog(self, package_name, language=None, kind='ihelp'):
        """Loads a catalog corresponding to package_name.
        """
        _debug("Loading %s catalog: '%s', lang=%s",
               kind, package_name, language)
        if language is None:
            language = str(self.language)
        key_tuple = (package_name, language, kind)
        # simply return if catalog is already loaded.
        if self.cache and key_tuple in self.cache.keys():
            cache_hit = self.cache[key_tuple]
            _debug("Catalog returned from cache at %s of type: %s",
                   id(cache_hit), type(cache_hit))
            return cache_hit
        # ... else, try to load catalog.
        catalog_modname = 'ihelp_%s__%s' %(language, package_name)
        try:
            catalog_module = __import__(catalog_modname)
        except ImportError:
            #sys.stderr.write('Warning: unable to load catalog module: %s\n'
            #                 %(catalog_modname))
            catalog_module = None
        # if catalog_module is valid, put it to cache.
        if catalog_module:
            if hasattr(catalog_module, kind):
                catalog = catalog_module.ihelp
                if self.cache is not None:
                    self.cache[(package_name, language, kind)] = catalog
            else:
                #sys.stderr.write('Warning: no ihelp in catalog: %s.\n'
                #                 %(catalog_modname))
                catalog = {}
        else:
            catalog = {}
        return catalog

    def load_catalog_bundle(self, bundle_name, language):
        """Loads bundle-type catalog.
        """
        _debug("Loading catalog bundle '%s', lang=%s", bundle_name, language)
        if language is None:
            language = str(self.language)
        # try to load bundle.
        bundle_modname = 'ihelpbundle_%s__%s' %(language, bundle_name)
        try:
            bundle_module = __import__(bundle_modname)
            _debug("Catalog bundle loaded: %s", bundle_module)
        except ImportError:
            sys.stderr.write('Warning: unable to load catalog bundle module: %s\n'
                             %(bundle_modname))
            bundle_module = None
            _debug("Failed to load catalog bundle: '%s', lang=%s",
                   bundle_name, language)
        # if bundle_module is valid, load bundled catalog.
        bundled_catalogs = {}
        if bundle_module:
            if hasattr(bundle_module, 'package_names'):
                package_names = bundle_module.package_names
                _debug("Catalog bundle: package_names=%s", package_names)
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
                        bundled_catalogs[(package_name, language, 'ihelp')] = catalog
                    else:
                        sys.stderr.write('Warning: no ihelp in catalog module: %s\n'
                                         %(catalog_modname))
        return bundled_catalogs

    def resolve_object_path(self, obj):
        """Determines package and name for given object.
        """
        _debug("Resolving object at %s of type:%s", id(obj), type(obj))
        mod_name, obj_name = None, None
        def get_mod_name(obj_, cls_, name_):
            # __doc__ may be provided in any base class.
            for base in reversed(getattr(cls_, '__bases__', [])):
                if (hasattr(base, name_) and
                    hasattr(getattr(base, name_), '__doc__') and
                    getattr(base, name_).__doc__==self._getdoc(obj)):
                    mod_name_ = inspect.getmodule(base).__name__
            return inspect.getmodule(cls_).__name__
        
        if inspect.ismodule(obj):
            _debug('INSPECT: object is a module.')
            # obj represents a module
            mod_name = obj.__name__
            obj_name = ''
        elif inspect.isclass(obj):
            _debug('INSPECT: object is a class.')
            mod_name = obj.__module__
            obj_name = obj.__name__
        elif hasattr(obj, '__objclass__'):
            _debug('INSPECT: object is an attrubute of class, resolved via __objclass__.')
            # object is bound as an attribute to some class.
            cls = obj.__objclass__
            obj_name = cls.__name__+'.'+obj.__name__
            mod_name = get_mod_name(obj, cls, obj_name)
        elif hasattr(obj, '__class__'):
            _debug('INSPECT: object is an attrubute of class, resolved via __objclass__.')
            cls = obj.__class__
            obj_name = cls.__name__+'.'+obj.__name__
            mod_name = get_mod_name(obj, cls, obj_name)
        else:
            _debug('INSPECT: object is something else.')
            # here, just give up understanding slithy internals.
            try:
                mod_name = inspect.getmodule(obj).__name__
                _debug('INSPECT: tried mod_name, %s', mod_name)
            except:
                pass
            try:
                obj_name = obj.__name__
                _debug('INSPECT: tried obj_name, %s', obj_name)
            except:
                pass

        if obj_name == None:
            raise ValueError('Failed to determine name for object at %s of type %s, attrs=%s' %(id(obj), type(obj), dir(obj)))
        if mod_name == None:
            raise ValueError('Failed to determine module name for object %s at %s of type %s, attrs=%s' %(obj_name, id(obj), type(obj), dir(obj)))

        _debug('INSPECTED: module %s, name %s', mod_name, obj_name)
        return mod_name, obj_name

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
                    # signature is None (use this translation anyway)
                    # ... or signature matches.
                    if signature in [None, doc_signature]:
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
        # laguage defaults to self.language.
        if language is None:
            language = self.language
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


def install(name, *args, **kwargs):
    """Installs ihelp.
    """
    import imp, sys
    # create getdoc instance
    getdoc_instance = GetDoc(*args, **kwargs)
    if '_ipydoc' in sys.modules:
        sys.modules.pop('_ipydoc')
    modfile = None
    try:
        modfile, fname, desc = imp.find_module('pydoc')
        ipydoc = imp.load_module('_ipydoc', modfile, '_ipydoc', desc)
    finally:
        if modfile:
            modfile.close()
    ipydoc.getdoc = getdoc_instance.getdoc
    # installs ihelp under __builtin__ namespace.
    import __builtin__
    setattr(__builtin__, name, ipydoc.Helper(sys.stdin, sys.stdout))


install('ihelp')
