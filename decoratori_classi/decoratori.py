# Assign functions to variables
def greet(name):
    return "Hello " + name

greet_someone = greet
print greet_someone("John")

# Define functions inside other functions
def greet1(name):
    def get_message():
        return "Hello "

    result = get_message()+name
    return result

print greet1("John")

# Functions can be passed as parameters to other functions
def greet2(name):
    return "Hello " + name

def call_func(func):
    other_name = "John"
    return func(other_name)

print call_func(greet2)

# Functions can return other functions
# In other words, functions generating other functions.
def compose_greet_func():
    def get_message():
        return "Hello John"
    return get_message

greet3 = compose_greet_func()
print greet3()

# Inner functions have access to the enclosing scope
# More commonly known as a closure
def compose_greet_func1(name):

    def get_message():
        # questa interna sa di "name" esterno
        return "Hello " + name

    return get_message

greet4 = compose_greet_func1("John")
print greet4()

# Function decorators are simply wrappers to existing functions
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

my_get_text = p_decorate(get_text)
print my_get_text("John")

# Come sopra ma usando i decoratori
def p_decorate1(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

@p_decorate1
def get_text1(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

print get_text1("John")

# Somma di decoratori
def p_decorate2(func):
   print func
   def func_wrapper(name):
       print "p" + name
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

def strong_decorate(func):
    print func
    def func_wrapper(name):
        print "strong" + name
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    print func
    def func_wrapper(name):
        print "div" + name
        return "<div>{0}</div>".format(func(name))
    return func_wrapper

# DOVREI FARE
    # get_text = div_decorate(p_decorate(strong_decorate(get_text)))
# MA INVECE CON I DECORATORI

@div_decorate
@p_decorate2
@strong_decorate
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

print get_text("John")

# Decorating Methods
def p_decorate3(func):
   def func_wrapper(self):
       return "<p>{0}</p>".format(func(self))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate3
    def get_fullname(self):
        return self.name + " " + self.family

my_person = Person()
print my_person.get_fullname()

# METTENDO *args e **kwargs nel WRAPPER della funzione lo generalizzo
# per accettare un qualisasi numero di parametri e funziona
# con functions and methods

def p_decorate_generalizzato(func):
   def func_wrapper(*args, **kwargs):
       return "<p>{0}</p>".format(func(*args, **kwargs))
   return func_wrapper

class Person1(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate_generalizzato
    def get_fullname(self):
        return self.name + " " + self.family

my_second_person = Person1()
print my_second_person.get_fullname()

# Passing arguments to decorators
def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("p")
def get_text_fin(name):
    return "Hello "+name

print get_text_fin("John")
print get_text_fin.__name__

# debug decorators
from functools import wraps
def tags1(tag_name):
    def tags_decorator1(func):
        @wraps(func)
        def func_wrapper1(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper1
    return tags_decorator1

@tags1("p")
def get_text_fin1(name):
    """returns some text che spiega la funzione"""
    return "Hello "+name

print get_text_fin1.__name__
print get_text_fin1.__doc__
print get_text_fin1.__module__

