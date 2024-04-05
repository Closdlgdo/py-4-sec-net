# we can see the code for finding the location of a given element inside a list. We use the range function to get
# elements inside protocolList and we compare each element with the element to find. When both elements are equal, we
# break the loop and return the element. To find out if an element is contained in a list, we can use the membership
# operator in.

my_list = [1, 2, 3, 4, 5]

print(1 in my_list)
print(6 in my_list)
print(6 not in my_list)