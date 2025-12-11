# Program of Palindrome

# [::-1] means “reverse”
#
# It reverses a:
#
# ✔ string
# ✔ list
# ✔ tuple
#
# Anything that supports slicing.
#
# 🔍 How it works?
#
# [start : stop : step]
#
# start → where to begin (blank = start of item)
#
# stop → where to end (blank = end of item)
#
# step → how to move (positive = forward, negative = backward)

def palindrome_value(numbers):
    if str(numbers) == str(numbers)[: : -1]:
        print("Given value is palindrome: ", numbers)
    else:
        print("Given number is not palindrome")

value =  input("Enter Ay numbers: ")
print(palindrome_value(value))
