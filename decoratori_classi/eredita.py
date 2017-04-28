class Parent(object):
    greeting = "Hello"


class Child(Parent):
    greeting = Parent.greeting + ' world'

class_test = Child()
print class_test.greeting
