def printExceptionsTree(ExceptionClass, level=0):
    if level > 1:
        print("   |" * (level - 1), end="")
    if level > 0:
        print("   +---", end="")
    print(ExceptionClass.__name__)
    for subclass in ExceptionClass.__subclasses__():
        printExceptionsTree(subclass, level + 1)


printExceptionsTree(BaseException)

# As a tree is a perfect example of a recursive data structure, a recursion seems to be the best tool to traverse
# through it. The printExceptionsTree() function takes two arguments:

# • A point inside the tree from which we start traversing the tree
# • A level to build a simplified drawing of the tree’s branches

# In the output of the previous script, we can see the root of Python’s exception classes is the BaseException class
# (this is a superclass of all the other exceptions). For each of the encountered classes, it performs the following
# set of operations:

# • Print its name, taken from the __name__ property.
# • Iterate through the list of subclasses delivered by the __subclasses__() method, an recursively invoke the
# printExceptionsTree() function, incrementing the nesting level, respectively.