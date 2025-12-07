# String
from dataclasses import replace

str1 = "Hello World"
str2 = "Automation Engineer is the key bone of every software company"
str3 = "  Chaudhary "
str4 = "A$#$#$#$"
str5 = ('34', '65', '34', '45')

#Case Conversion:
print("#Case Conversion:")

print(str1.lower())
print(str1.upper())
print(str1.capitalize())
print(str1.title())
print(str2.swapcase())

# Whitespace and Character Removal
print("#Whitespace and Character Removal")

print(str3.strip())
print(str3.lstrip())
print(str3.rstrip())

# Searching and Replacing
print("#Searching and Replacing")

print(str2.find("company"))
print(str1.find("World"))
print(str2.replace("bone","root"))

# Splitting and Joining:
print("#Splitting and Joining:")

print(str2.split())
print(str2.split(" . "))
print(str1.join(str3))

#Checking String Content:
print("#Checking String Content:")

print(str2.startswith("Automation"))
print(str1.endswith("Chaudhary"))
print(str4.isalpha())
#print(str5.isdigit())
#print(str5.isalnum())


