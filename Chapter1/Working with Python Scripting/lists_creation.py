# Lists in Python are, used to store sets of related items of the same or different types. Also, a list is a mutable
# data structure which allows the list content can be modified after it has been created.
# Example:
response = [200, 400, 403, 404, 500]

print(response)

# Indexes are used to access an element of a list. An index is an integer that indicates the position
# of an element in a list. The first element of a list always starts at index 0.

print(response[0])
print(response[1])
print(response[2])
print(response[3])
print(response[4])

# If an attempt is made to access an index that is outside the range of the list, the interpreter will throw the
# IndexError exception. Similarly, if an index that is not an integer is used, the TypeError exception will be thrown.