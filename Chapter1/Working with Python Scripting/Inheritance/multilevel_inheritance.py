# we are implementing multilevel inheritance where the child class is inheriting from the MainClass and we add another
# level of inheritance with the ChildDerived class, which is inheriting from the Child class.

class MainClass:
    def message_main(self):
        print('Welcome to Main Class')


class Child(MainClass):
    def message_child(self):
        print('Welcome to Child Class')
        print('This is inherited from Main')


class ChildDerived(Child):
    def message_derived(self):
        print('Welcome to Derived Class')
        print('This is inherited from Child')

# In the previous code we first create a main class and then create a child class that is inherited from Main and
# create another class derived from the child class. We see how the child_derived_obj object is an instance of each of
# the classes that are part of the hierarchy. In multilevel inheritance, the features of the base class and the derived
# class are inherited into the new derived class. In our main program we declare a child-derived object and we call the
# methods defined in each of the classes.


if __name__ == '__main__':
    child_derived_obj = ChildDerived()
    child_derived_obj.message_main()
    child_derived_obj.message_child()
    child_derived_obj.message_derived()
    print(issubclass(ChildDerived, Child))
    print(issubclass(ChildDerived, MainClass))
    print(issubclass(Child, MainClass))
    print(issubclass(MainClass, ChildDerived))
    print(isinstance(child_derived_obj, Child))
    print(isinstance(child_derived_obj, MainClass))
    print(isinstance(child_derived_obj, ChildDerived))
