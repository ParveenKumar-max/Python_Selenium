# Practise of Armstrong number

# A number is Armstrong if the sum of each digit raised to the power
# of the number of digits equals the number itself.

# 1³ + 5³ + 3³
# = 1 + 125 + 27
# = 153
# *********************
# 9⁴ + 4⁴ + 7⁴ + 4⁴
# = 6561 + 256 + 2401 + 256
# = 9474

value = input("Enter Any numbers: ")
digits = len(value)
print(digits)

sum_of_power = 0

for number in value:
    sum_of_power = sum_of_power + (int(number) ** digits)

if sum_of_power == int(value):
    print(value, "is an armstrong")
else:
    print(value,"is not an armstrong")
