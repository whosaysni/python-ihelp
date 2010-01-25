import pydoc, inspect, sys

MODULES = [
    'simplejson',
    ]

pydoc._getdoc = pydoc.getdoc

def dump_doc(object):
    s = ''
    s += repr(object)
    s += str([inspect.getmodulename(object)])
    s += str(inspect.getmodule(object))
    s += str(object.__name__)
    s += pydoc._getdoc(object)
    sys.stderr.write(s)
    return s

pydoc.getdoc = dump_doc
        
import StringIO

o = StringIO.StringIO()
pydoc.help = pydoc.Helper(sys.stdin, o)
for mod in MODULES:
    pydoc.help(mod)
print o.getvalue()
        
    
