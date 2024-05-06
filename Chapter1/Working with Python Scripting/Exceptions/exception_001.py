# a + 4
# NameError: name 'a' is not defined

# "4" + 4
# TypeError: can only concatenate str (not "int") to str

try:
    print("10/0=", str(10/0))
except Exception as exception:
    print("Error =", str(exception))

# Error = division by zero

# The try keyword begins a block of the code that may or may not be performing correctly. Next, Python tries to perform
# some operations; if it fails, an exception is raised, and Python starts to look for a solution.

# At this point, the except keyword starts a piece of code that will be executed if anything inside the try block goes
# wrong – if an exception is raised inside a previous try block, it will fail here, so the code located after the except
# keyword should provide an adequate reaction to the raised exception. The following code raises an exception related to
# accessing an element that does not exist in the list:

try:
    list = []
    element = list[0]
except Exception as exception:
    print("Error =", str(exception))

# Error = list index out of range