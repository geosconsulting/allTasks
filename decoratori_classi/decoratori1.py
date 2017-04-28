a_string = "This is a global variable"
def foo():
    print locals()
print globals() # doctest: +ELLIPSIS

# quella dentro conosce la variabile di quella fuori
def outer():
    x = 1
    def inner():
        print x # 1
    return inner() # 2
print outer()

# OPPURE
def outer1():
    x = 1
    def inner1():
         print x # 1
    return inner1
foo = outer1()
print foo
print foo()

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Coord: " + str(self.__dict__)

def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)

def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)

one = Coordinate(100, 200)
two = Coordinate(300, 200)
three = Coordinate(-100, -100)

print sub(one, two)
print add(one, three)

def wrapper(func):
    def checker(a, b): # 1
        if a.x < 0 or a.y < 0:
            a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
        if b.x < 0 or b.y < 0:
            b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        ret = func(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
        return ret
    return checker

add = wrapper(add)
sub = wrapper(sub)

print sub(one, two)
print add(one, three)


#  Instead of add = wrapper(add) we can "decorate" it with the @ symbol like:
@wrapper
def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)
print add(one, three)


# in order to make it more general
def one(*args):
    print args

print one()
print one(1, 2, 3)


def two(x, y, *args):
    print x, y, args
print two('a', 'b', 'c')


def add(x, y):
    return x + y
lst = [1, 2]
print add(lst[0], lst[1])
print add(*lst)

def foo_k(**kwargs):
    print kwargs
print foo_k()

print foo_k(x=1, y=2)

def foo_string(**kwargs):
    print kwargs

dict = {'nome': 'Pippo', 'cognome': 'Palla'}
print foo_string(**dict)

def foo_string_1(nome, cognome):
    return nome + " - " + cognome
print foo_string_1(**dict)

def logger(func):
    def inner(*args, **kwargs): #1
        print "Arguments were: %s, %s" % (args, kwargs)
        return func(*args, **kwargs) #2
    return inner

@logger
def foo100(x, y=1):
    return x * y

@logger
def foo200():
    return 2

print foo100(5, 4)
print foo100(1)
print foo200()

def entryExit(f):
    def new_f():
        print "Entering", f.__name__
        f()
        print "Exited", f.__name__
    return new_f

@entryExit
def func1():
    print "inside func1()"

@entryExit
def func2():
    print "inside func2()"

func1()
func2()
print func1.__name__
