# Convert String To Integer


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
    # Built-in function,
    # Raised when an operation or function receives an argument that has the right type but an inappropriate value.
    print("Incorrect value", value_inter1)