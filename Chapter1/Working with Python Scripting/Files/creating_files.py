# There are multiple ways to open and create files in Python, but the safest way is by using the with keyword, in which
# case we are using the Context Manager approach. When we are using the open statement, Python delegates to the developer
# the responsibility for closing the file, and this practice can provoke errors since developers sometimes forget to close it.

# Developers can use the with statement to handle this situation in a safe way. The with statement automatically closes
# the file even if an exception is raised. Using this approach, we have the advantage that the file is closed
# automatically, and we don’t need to call the close() method.

def main():
    with open('test.txt', 'w') as file:
        file.write("this is a test file")
    if __name__ == '__main__':
        main()