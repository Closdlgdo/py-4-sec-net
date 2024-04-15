class Protocol(object):
    def __init__(self, name, number,description):
        self.name = name
        self.number = number
        self.description = description

    def getProtocolInfo(self):
        return self.name+ " "+str(self.number)+ " "+self.description


# The init method is a special method that acts as a constructor method to perform the necessary initialization
# operation. The method’s first parameter is a special keyword, and we use the self-identifier for the current object
# reference. The self keyword is a reference to the object itself and provides a way for its attributes and methods to
# access it.
# The constructor method must provide the self parameter and may have more parameters than just self; if this happens,
# the way in which the class name is used to create the object must reflect the __init__ definition. This method is used
# to set up the object, in other words, to properly initialize its internal state. This parameter is equivalent to the
# pointer that can be found in languages such as C ++ or Java.

# An object is a set of requirements and qualities assigned to a specific class. Classes form a hierarchy, which means
# that an object belonging to a specific class belongs to all the superclasses at the same time.