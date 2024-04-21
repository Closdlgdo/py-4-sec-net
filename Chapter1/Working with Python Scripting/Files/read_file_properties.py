file_descryptor = open("read_file_properties.py", "r+")
print("Content: "+file_descryptor.read())
print("Name: "+file_descryptor.name)
print("Mode: "+file_descryptor.mode)
print("Encoding: "+str(file_descryptor.encoding))
file_descryptor.close()

# When reading a file, the readlines() method reads all the lines of the file and joins them in a list sequence. This
# method is very useful if you want to read the entire file at once:

print("Lines: ")
for line in file_descryptor.readlines():
    print(line.strip())