c = 20
d = 40
e = 50

class Foo(object):
    def __init__(self, *args, **kwargs):
        print('Instantiating: {} {}'.format(args, kwargs))
