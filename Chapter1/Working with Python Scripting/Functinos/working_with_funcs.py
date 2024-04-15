# we can define a function that returns True if the item value is found in the dictionary and False otherwise.
# You can find the following code in the my_function.py file:

def contains(diction, item):
    for key,value in diction.items():
        if value == item:
            return True\

    return False


diction = {1:100,2:200,3:300}

print(contains(diction,200))
print(contains(diction,300))
print(contains(diction,350))