# A prime number is:
#
# ✔ A number greater than 1
# ✔ That has only two factors: 1 and the number itself
# ✔ It cannot be divided evenly by any other number
#
# Examples:
#
# Prime numbers: 2, 3, 5, 7, 11, 13
#
# Not prime numbers: 4 (divisible by 2), 6, 8, 9, 12

def is_prime(num):
    if num <= 1:
        return False
        #print("Number is not Prime: ", num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Find the prime range from given number

def find_primes(start, end):
    prime_num = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_num.append(num)
    return prime_num

value = int(input("Enter Any Numbers: "))
value1 = int(input("Enter Any Numbers: "))
print("Check Value is prime", find_primes(value, value1))

