# Like lists, the tuple class in Python is a data structure that can store elements of different types. Along with the
# list and range classes, it is one of the sequence types in Python, with the particularity that they are immutable.
# This means its content cannot be modified after it has been created.
# In general, to create a tuple in Python, you simply define a sequence of elements separated by commas.
# Indices are used to access an element of a tuple. An index is an integer indicating the position of an element in a
# tuple. The first element of a tuple always starts at index 0.

# Create a tuple
my_tuple = (1, 2, 3, 'a', 'b', 'c')

# Access elements of the tuple using indices
first_element = my_tuple[0]
third_element = my_tuple[2]
last_element = my_tuple[-1]

# Print the elements
for element in my_tuple:
    print(element)


the_tuple = ("FTP", "HTTP", "SNMP", "SSH")

print(the_tuple)