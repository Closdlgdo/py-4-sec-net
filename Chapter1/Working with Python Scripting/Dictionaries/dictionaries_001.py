# The Python dictionary data structure is probably the most important in the entire language and allows us to associate
# values with keys. Python’s dict class is a map type that maps keys to values. Unlike sequential types (list, tuple,
# range, or str), which are indexed by a numeric index, dictionaries are indexed by keys. Among the main features of the
# dictionaries, we can highlight:
# • It is a mutable type, that is, its content can be modified after it has been created.
# • It is a type that reserves the order in which key-value pairs are inserted.
# In Python there are several ways to create a dictionary. The simplest is to enclose a sequence of comma-separated
# key:value pairs in curly braces {}. In this example we will define the service name as the key and the port number as
# the value.

my_dict = {"FTP": 21, "HTTP": 80, "HTTPS": 443, "SSH": 22}

print(my_dict)
