# Factorial

def factorial(numbers):
    if numbers == 1:
        return 1
    return numbers * factorial(numbers - 1)
print("Value of Factorial", factorial(5))


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