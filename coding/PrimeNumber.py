# Check the Prime Number

# Prime numbers must be greater than 1
#  if n <= 1:
#         return False
# If n is 1, 0, or negative, the function immediately returns False, meaning “not prime”.
# n**0.5  --> square of the value that user entered.


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test
num = int(input("Enter a number: "))
print(num, "is prime?" , is_prime(num))
