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
