# In the following example, we are using the readlines() method to process the file and get counts of the lines and
# characters in this file.

try:
    countlines = countchars = 0
    file = open('count_lines_chars.py', 'r')
    lines = file.readlines()
    for line in lines:
        countlines += 1
        for char in line:
    file.close()
    print("Characters in file:", countchars)
    print("Lines in file:", countlines)
except IOError as error:
    print("I/O error occurred:", str(error))

# If the file we are reading is not available in the same directory, then it will throw an I/O exception with the following error message:
#    I/O error occurred: [Errno 2] No such file or directory: 'newfile.txt'