# How if else works in Python
Greeting_Name = "Good Morning"  # string variable
b = 45  # int type variable

if (Greeting_Name == "Good Morning"):
    print("Value present in the Greeting_Name is true")
    print("Checking another condition") # Try to add else condition
elif (b == 45):
    print("Value is Matched")
else:
    print("Learning If else")
print("Checking if else condition in python")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("================================================================")

if b < 45:
    print("Adult")
elif b > 45:
    print("Seniour Citizen")
elif b == 45:
    print("Same age")
else:
    print("No Input")
print("Checking age of the person")

# In Python, there is no Scanner class — instead, we use the built-in input() function.

name = input("Enter your name: ")
print("Hello,", name)