# An object is a set of requirements and qualities assigned to a specific class. Classes form a hierarchy, which means
# that an object belonging to a specific class belongs to all the superclasses at the same time.
# To build an object, write the class name followed by any parameter needed in parentheses. These are the parameters
# that will be transferred to the init method, which is the process that is called when the class is instantiated

class MyProtocol:
    def __init__(self, parameter):
        self.parameter = parameter


# This code defines a constructor method for a Python class that initializes an instance variable called parameter with
# the value passed to the constructor.

# we can access its attributes and methods through the object. attribute and object.method() syntax

obj = MyProtocol("HTTPServer")
print(obj.parameter)

# object programming is the art of defining and expanding classes. A class is a model of a very specific part of
# reality, reflecting properties and methods found in the real world. The new class may add new properties and new
# methods, and therefore may be more useful in specific applications.