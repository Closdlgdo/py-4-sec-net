# Another interesting operation that we perform in lists is the one that offers the possibility of getting elements in a
# reverse way in the list through the reverse() method.

my_list = [1, 2, 3, 4, 5]

print(my_list)

my_list.reverse()

print(my_list)

# Another way to do the same operation is to use the -1 index. This quick and easy technique shows how you can access
# all the elements of a list in reverse order:

for item in my_list[::-1]:
    print(item)