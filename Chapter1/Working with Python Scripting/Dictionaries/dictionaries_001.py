# The Python dictionary data structure is probably the most important in the entire language and allows us to associate
# values with keys. Python’s dict class is a map type that maps keys to values. Unlike sequential types (list, tuple,
# range, or str), which are indexed by a numeric index, dictionaries are indexed by keys. Among the main features of the
# dictionaries, we can highlight:
# • It is a mutable type, that is, its content can be modified after it has been created.
# • It is a type that reserves the order in which key-value pairs are inserted.
# In Python there are several ways to create a dictionary. The simplest is to enclose a sequence of comma-separated
# key:value pairs in curly braces {}. In this example we will define the service name as the key and the port number as
# the value.
import services

my_dict = {"FTP": 21, "HTTP": 80, "HTTPS": 443, "SSH": 22}

print(my_dict)

print(my_dict["FTP"])

# Accessing an element of a dictionary is one of the main operations for which this type of data exists.
# Access to a value is done by indexing the key. To do this, simply enclose the key in square brackets.
# If the key does not exist, the KeyError exception will be thrown.
another_dict = dict(TCP=6, UDP=17, ICMP=1)
print(another_dict)

# The dict class also offers the get (key[, default value]) method. This method returns the value corresponding to the
# key used as the first parameter. If the key does not exist, it does not throw any errors, but returns the second
# argument by default. If this argument is not supplied, the value None is returned.

print(my_dict.get("FTP"))
print(my_dict.get("SMTP"))
print(my_dict.get("SMTP", "Port not found"))

# Using the update method, we can combine two distinct dictionaries into one. In addition, the update method will merge
# existing elements if they conflict.
my_dict.update(another_dict)
print(my_dict)

services = {"FTP": 21, "HTTP": 80, "HTTPS": 443, "SSH": 22}
services2 = {"FTP": 2121, "DNS": 53, "SMTP": 25}
services.update(services2)
print(services)

# The first value is the key, and the second the key value. We can use any unchangeable value as a key. We can use
# numbers, sequences, Booleans, or tuples, but not lists or dictionaries, since they are mutable.
# The main difference between dictionaries and lists or tuples is that values contained in a dictionary are accessed
# by their name and not by their index. You may also use this operator to reassign values, as in the lists and tuples.
# Creating a dictionary with a tuple key and a string value
my_dict = {(1,2): "value"}
# Creating a dictionary with a boolean key and an integer value
another_dict = {True: 1, False: 0}
# Creating a dictionary with a sequence key and a float value
third_dict = {("a", "b", "c"): 3.14}
# Reassigning values in a dictionary
my_dict[(1, 2)] = "new value"
another_dict[True] = 100