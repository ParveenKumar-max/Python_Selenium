# Handle Exception

#try:
      # Code
#except SomeException:
      # Code
#else:
     # Code
#finally:
    # Code

def exception_check(set_value):
    if set_value <= 0:
        raise ValueError("Negative numbers are not allowed")
    return set_value

try:
    my_number = int(input("Enter any numbers "))
    exception_check(my_number)
    print(f"Valid Number: {my_number}")
except ValueError:
    print("Invalid input")
