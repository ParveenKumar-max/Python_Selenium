with open('/Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))

    data = testwritefile.read()
    if (not data):  # empty strings return false in python
        print('Read nothing')
    else:
        print(testwritefile.read())

    testwritefile.seek(0, 0)  # move 0 bytes from beginning.

    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data):
        print('Read nothing')
    else:
        print(data)

    print("Location after read: {}".format(testwritefile.tell()))


# r+ : Reading and writing. Cannot truncate the file.
# w+ : Writing and reading. Truncates the file.
# a+ : Appending and Reading. Creates a new file, if none exists.
# You dont have to dwell on the specifics of each mode for this lab.


with open('/Example2.txt', 'r+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    testwritefile.seek(0,0)
    print(testwritefile.read())