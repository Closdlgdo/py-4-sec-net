# a + 4
# NameError: name 'a' is not defined

# "4" + 4
# TypeError: can only concatenate str (not "int") to str

try:
    print("10/0=", str(10/0))
except Exception as exception:
    print("Error =", str(exception))

# Error = division by zero