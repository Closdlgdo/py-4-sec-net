# Lists are mutable sequences that can be modified, which means items can be added, updated, or removed.
# To add one or more elements, we can use the extend() method. Also, we can use the insert() method to insert an element
# in a specific index location. We can add elements to a list by means of the following methods:
# • list.append(value): This method allows an element to be inserted at the end of the list. It takes its argument’s
# value and puts it at the end of the list that owns the method. The list’s length then increases by one.
# • list.extend(values): This method allows inserting many elements at the end of the list.
# • list.insert(location, value): The insert() method is a bit smarter since it can add a new element at any place in
# the list, not just at the end. It takes as arguments first the required location of the element to be inserted and then
# the element to be inserted.

my_list = [1, 2, 3, 4, 5]
my_list.extend([6, 7, 8])
my_list.insert(2, 10)
my_list.append(5)

print(my_list)