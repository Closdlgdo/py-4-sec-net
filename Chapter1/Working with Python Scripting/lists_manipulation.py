# Lists also provide methods that help manipulate the values within them and allow us to store more than one variable
# within them and provide a better way to sort object arrays in Python. These are the techniques commonly used to manage
# lists.
protocols = []
# • .append(value): Appends an element at the end of the list
protocols.append("HTTPS")
protocols.append("SSH")
protocols.append("Telnet")
protocols.append("SMTP")
protocols.append("POP3")
protocols.append("IMAP4")
protocols.append("NTP")

print(protocols)
# • .copy(): Returns a copy of the list
protocols_copy = protocols.copy()
# • .extend('x'): Adds all elements of 'x' to the end of the list
protocols.extend(protocols_copy)
print(protocols)
# • .count('x'): Gets the number of 'x' elements in the list
print(protocols.count("HTTPS"))
# • .index('x'): Returns the index of 'x' in the list
print(protocols.index("IMAP4"))
# • .insert('y','x'): Inserts 'x' at location 'y'
protocols.insert(1, "HTTP")
print(protocols)
# • .pop(): Returns the last element and removes it from the list
print(protocols.pop())
# • .remove('x'): Removes the first 'x' from the list
print(protocols.remove("HTTPS"))
# • .reverse(): Reverses the elements in the list
print(protocols.reverse())
# • .sort(): Sorts the list in ascending order
print(protocols.sort())
print(protocols)
# • .clear(): Removes all elements from the list
print(protocols.clear())