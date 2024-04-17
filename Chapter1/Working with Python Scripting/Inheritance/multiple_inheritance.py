# Multiple inheritance occurs when a child class inherits attributes and methods from more than one parent class. We
# could separate both main classes with a comma when creating the secondary class. In the following example we are
# implementing multiple inheritance where the child class is inheriting from the MainClass and MainClass2 classes.

class MainClass:
    pass


class MainClass2:
    pass


class SecondaryClass(MainClass, MainClass2):
    pass