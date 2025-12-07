# Read and write the file

file = open('TestFile.txt')   # Open the File.

#print(file.read())   # Read all the contents of file

#print(file.read(2))     # Read n number of characters by passing parameter

#print(file.readline())    # Read one single at a time, if you have paragraph you can print line by line via readline
#print(file.readline())

line_value = file.read()
while line_value != "":
   print(line_value)      # Program will be stuck in infinite loop, so we have to put exist condition.
   line_value = file.read()

# Now we will work with for loop

for line in file.readlines():
    print(line)

# How to work with list
values = ['abc', 'xyz', 'qwe', 'tyu', 'uiop']
for i in values:
    print(i)


file.close()