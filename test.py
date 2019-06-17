#!/usr/bin/env python
# pylint: disable=redefined-builtin
"""
reimportlib: refactored imports
"""
import reimportlib
__import__ = reimportlib.import_

reimportlib.configure() # Reads mappings in .reimport.json
reimportlib.remap('foo', 'examples.bar') # Remap Individually
reimportlib.remap('foo.bar', 'examples.baz')
reimportlib.remap('foo.bar.', 'examples.foo.') # Notice the . at the end

print(reimportlib.get_remapped_name('foo.A')) # 'examples.bar.A'
print(reimportlib.get_remapped_name('foo.bar')) # 'examples.baz'
print(reimportlib.get_remapped_name('foo.bar.C')) # 'examples.foo.C'

__import__('foo.bar')
print(reimportlib.import_module('foo.bar.B'))
print(reimportlib.import_from('foo.bar.D', 'c'))
reimportlib.instantiate('foo.bar.D', 'Foo', *[4], val=True)
