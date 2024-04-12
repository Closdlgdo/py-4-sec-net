# Each key must be unique: That means it is not possible to have more than one key of the same value.
# • A key may be a number or a string.
# • A dictionary is not a list: A list contains a set of numbered values, while a dictionary
# holds pairs of values.
# • The len() function: This works for dictionaries and returns the number of key-value elements in the dictionary.

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(len(my_dict))

# We can use the keys() method to get a list of all the keys in the dictionary.

print(my_dict.keys())

# The dict class implements three methods, since they return an iterable data type, known as view objects. These objects
# provide a view of the keys and values of type dict_values contained in the dictionary, and if the dictionary changes,
# these objects are instantly updated. The methods are as follows:
# • items(): Returns a view of (key, value) pairs from the dictionary.
# • keys(): Returns a view of the keys in the dictionary.
# • values(): Returns a view of the values in the dictionary.

print(my_dict.items())

print(my_dict.values())

print("--------------------------------")

for key, value in my_dict.items():
    print(key, value)