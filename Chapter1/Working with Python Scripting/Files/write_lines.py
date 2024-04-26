#  Writing text files is possible using the write() method and it expects just one argument that represents a string
#  that will be transferred to an open file.

try:
    myfile = open('newfile.txt', 'wt')
    for i in range(10):
        myfile.write("line #" + str(i+1) + "\n")
    myfile.close()
except IOError as error:
    print("I/O error occurred: ", str(error.errno))