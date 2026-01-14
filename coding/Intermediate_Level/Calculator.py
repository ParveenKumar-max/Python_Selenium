# Calculator

def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return  a * b
    elif operation == "division":
        return a / b
    elif operation == "modulus":
        return a % b

    else:
        return "Invalid operation"

print(calculator(5,6,"add"))
print(calculator(15,26,"subtract"))
print(calculator(15,36,"division"))
print(calculator(5,6,"multiply"))
print(calculator(45,46,"modulus"))