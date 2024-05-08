# we join all these functionalities with exception management when we are working with files. If the file is not found
# in the filesystem, an exception of the IOError type is thrown, which we can capture thanks to our try-except block.

try:
    file_handle = open("myfile.txt", "r")
except IOError as exception:
    print("Exception IOError: Unable to read from myfile ", exception)
except Exception as exception:
    print("Exception: ", exception)
else:
    print("File read successfully")
    file_handle.close()

# we manage an exception when opening a file in read mode and if the file does not exist it will throw the message
# \"Exception IOError: Unable to read from myfile [Errno 2] No such file or directory: 'myfile.txt'".