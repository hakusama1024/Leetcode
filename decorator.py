class A(object):
    def foo(self, n):
        print n

def do(func, arg):
    print 'hello'
    func(arg)

a = A()
do(a.foo, 1)
