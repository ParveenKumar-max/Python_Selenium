# Factorial program with different way

# The factorial of a number n (written as n!) is the product of all positive integers from 1 to n



def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)
value = int(input("Enter any number: "))
print("Number of", value, "is factorial", factorial(value))


#5 × 4 = 20
#20 × 3 = 60
#60 × 2 = 120
#120 × 1 = 120

#n! = n × (n − 1)!

# 5! = 5 × 4!
# 4! = 4 × 3!
# 3! = 3 × 2!
# 2! = 2 × 1!
# 1! = 1

value = int(input("Enter any number: "))
facto = 1
if value < 1:
    print("Value is not factorial")
else:
    for i in range(1, value + 1):
        facto = facto * i

print("Number of", value, "is factorial", facto)

