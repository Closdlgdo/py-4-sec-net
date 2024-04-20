# The open() function is usually used with two parameters (the file with which we are going to work and the access mode)
# and it returns a file-type object. When opening a file with a certain access mode with the open() function, a file
# object is returned.
# The opening modes can be r (read), w (write), and a (append). We can combine the previous modes with others depending
# on the file type. We can also use the b (binary), t (text), and + (open reading and writing) modes. For example, you
# can add a + to your option, which allows read/ write operations with the same object:
file = open("example.txt", "w+")

print(file)

file.close()