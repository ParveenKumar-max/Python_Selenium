# Fibonacci series is a sequence of numbers where:
#
# 👉 Each number = sum of previous two numbers

value = int(input("Enter sny Numbers: "))

a,b = 0, 1

print("Fibonacci Series starts")

for _ in range (value):
    print(a, end=" ")
    a, b = b, a + b