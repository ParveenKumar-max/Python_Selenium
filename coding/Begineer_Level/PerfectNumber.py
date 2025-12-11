# Practice of Perfect number

# A perfect number is a number that is equal to the sum of all its proper divisors (excluding itself).

# Example for 28:
# Divisors: 1, 2, 4, 7, 14 → (exclude 28)

value = int(input("Enter Any numbers: "))
sum_of_numbers = 0

for i in range(1, value):
    if value % i == 0:
        sum_of_numbers = sum_of_numbers + i

if sum_of_numbers == value:
    print("The given value is Perfect Number")
else:
    print("The given value is not a Perfect Number")