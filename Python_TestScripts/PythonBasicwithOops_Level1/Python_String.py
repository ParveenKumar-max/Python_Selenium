# String

str1 = "Parveen Chaudhary"
str2 = "Senior Automation Engineer"
a = 9
stringCompare = "Chaudhary "



print(str1[1]) # It will print only a --> same indexing format star from 0 to str-1

print(str1[0 : 7]) #print the value from 0 to n-1,

print(str1 + " : ",  str2)  # Easily concatenate two string using

print(f"{str1}:{str2}, Having {a} of experience.")  # This is the best way to concatenate string and int.

print(stringCompare.strip())  # strip function is used to remove the extra white space from string
print(stringCompare in str1)   # The match is fail because stringCompare String having 1 white space on right side.

removeWhiteSpace = stringCompare.strip() # Remove the extra white space, stored in the variable.
print(removeWhiteSpace)
print(removeWhiteSpace in str1)  # Now condition will True.

print(str1.split(" "))
splitValue = str1.split(" ")  # If want to split it from white space, then it will count whole string as a 0 index.
print(splitValue)
print(splitValue[0])

print(list(str1)) # it will print whole string in list.

print(str1.split(" ", 2))

print(str1.split(","))

print(str1.split())