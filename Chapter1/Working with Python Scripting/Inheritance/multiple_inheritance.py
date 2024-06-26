# Multiple inheritance occurs when a child class inherits attributes and methods from more than one parent class. We
# could separate both main classes with a comma when creating the secondary class. In the following example we are
# implementing multiple inheritance where the child class is inheriting from the MainClass and MainClass2 classes.

class MainClass:
    def message_main(self):
        print('Welcome to Main Class')


class MainClass2:
    def message_main2(self):
        print('Welcome to Main Class2')


class ChildClass(MainClass,MainClass2):
    def message(self):
        print('Welcome to ChildClass')
        print('This is inherited from MainClass and MainClass2')


if __name__ == '__main__':
    child_obj = ChildClass()
    child_obj.message()
    child_obj.message_main()
    child_obj.message_main2()

# Output:
# Welcome to ChildClass
# This is inherited from MainClass and MainClass2
# Welcome to Main Class
# Welcome to Main Class2