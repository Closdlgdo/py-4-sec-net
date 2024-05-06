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