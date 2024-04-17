# Single inheritance occurs when a child class inherits the attributes and methods of a single parent class. The
# following is an example of simple inheritance in Python where we have a base class and a child class that inherits
# from the parent class. Note the presence of the __init__ method in both classes , which allows you to initialize the
# properties of the class as an object constructor.

class BaseClass:
    def __init__(self, property):
        self.property = property

    def message(self):
        print('Welcome to Base Class')

    def message_base_class(self):
        print('This is a message from Base Class')


class ChildClass(BaseClass):
    def __init__(self, property):
        BaseClass.__init__(self, property)

    def message(self):
        print('Welcome to ChildClass')
        print('This is inherited from BaseClass')

# In our main program we declare two objects, one of each class, and we call the methods defined in each of the classes.
# Also, taking advantage of the inheritance features, we call the method of the parent class using an object of the
# child class.