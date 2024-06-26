# create a list using the append() method by adding objects, printing the objects, and then sorting them before printing
# again. We describe a list of protocols in the following example, and use the key methods of a Python list, such as
# add, index, and remove.

protocols = []

protocols.append("HTTP")
protocols.append("SSH")
protocols.append("Telnet")
protocols.append("SMTP")

print(protocols)

protocols.sort()

print(type(protocols))
print(len(protocols))

print(protocols)

# To access specific positions, we can use the index() method, and to delete an element, we can use the remove() method.

print(protocols[0])
print(protocols[1])
print(protocols[2])
print(protocols[3])

protocols.remove("SSH")
print(len(protocols))

print(protocols)

# To print out the whole protocol list, use the following instructions. This will loop through all the
# elements and print them out one by one.

for protocol in protocols:
    print(protocol)

# To do this in a more efficient way, we can use the enumerate() function. The enumerate() function returns
# an object that contains a list of tuples, where each tuple contains a count (from 0) and an element from the list.
for count, protocol in enumerate(protocols):
    print(count, protocol)

# To do this in a more efficient way, we can use list comprehension. The list comprehension is an efficient way more efficient
protocol_lengths = [len(protocol) for protocol in protocols]
print(protocol_lengths)