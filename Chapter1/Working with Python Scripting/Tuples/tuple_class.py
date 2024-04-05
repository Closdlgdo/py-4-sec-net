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

print("--------------------------")

the_tuple = ("FTP", "HTTP", "SNMP", "SSH")

print(the_tuple)

print("--------------------------")
# If an attempt is made to access an index that is outside the range of the tuple, the interpreter will throw the
# IndexError exception. Similarly, if an index that is not an integer is used, the TypeError exception will be thrown:

print(the_tuple[0])
print(the_tuple[1])
print(the_tuple[2])
print(the_tuple[3])
# print(the_tuple[4]) # IndexError: tuple index out of range

print("--------------------------")
# As with lists and all sequential types, it is permissible to use negative indices to access the elements of a tuple.
# In this case, the index -1 refers to the last element of the sequence, -2 to the penultimate, and so on:

print(the_tuple[-1])
print(the_tuple[-2])
print(the_tuple[-3])
print(the_tuple[-4])
