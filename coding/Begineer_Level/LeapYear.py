# Leap year practise

# A year is a leap year if any one of the following is true:
#
# ✔ Rule 1
#
# The year is divisible by 4 ( 2025 / 4 )
#
# AND
#
# ✔ Rule 2
#
# If the year is divisible by 100, it must also be divisible by 400. ( if 2025 / 100, must be 2025 / 400 )

value = input("Enter the number: ")
year = int(value)
if year % 4 == 0:
    print(year, "is a leap year")
elif year % 100 == 0:
    print(year,"is not a leap year")
elif year % 400 == 0:
    print(year,"is a leap year")
else:
    print(year, "is incorrect number")