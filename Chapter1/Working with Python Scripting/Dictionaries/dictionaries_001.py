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