# Convert String To Inetger
from unicodedata import decimal

value_text = input(" Enter the value : ")
if value_text.isdigit():
    value_inter = int(value_text)
    print("Entered value is number", value_inter)
else:
    print("Entered value is character", value_text)

print(type(value_inter))

# Handle through Try and catch

value_text1 = input("Enter any value : ")
try:
    value_inter1 = int(value_text1)
    print("Converted value is :", value_inter1)
except ValueError:
    print("")