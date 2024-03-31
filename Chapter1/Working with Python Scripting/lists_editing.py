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