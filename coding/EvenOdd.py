# Even or Odd
# input --> CLI option or  build in function we use to take the input from user

value = int(input("Enter the numbers : "))

if  value % 2 == 0:
    print("Value is even")
else:
    print("Value is Odd")

# Through Method Creation
# If it's even, Print True else False
def Even_odd(number):
    return number % 2 == 0

print(Even_odd(23456789))
print(Even_odd(98743456098765))

