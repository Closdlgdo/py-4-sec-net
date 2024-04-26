#  Writing text files is possible using the write() method and it expects just one argument that represents a string
#  that will be transferred to an open file.

try:
    myfile = open('newfile.txt', 'wt')
    for i in range(10):
        myfile.write("line #" + str(i+1) + "\n")
    myfile.close()
except IOError as error:
    print("I/O error occurred: ", str(error.errno))

# The write() method is very useful if we want to write a string to a file at a certain location.
myfile.write("This is a new line being added to the file.\n")
# If we want to write multiple lines, we can use the writelines() method. This method takes a list of strings as an

# example:
with open('newfile.txt', 'a') as myfile:
    lines = ["New line 1\n", "New line 2\n", "New line 3\n"]
    myfile.writelines(lines)
