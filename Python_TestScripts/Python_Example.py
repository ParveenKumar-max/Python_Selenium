# Handle Tuple modification exception with Try Catch

person = ("Rahul", 25, 9.5)
print(f"Age is: {person[0]}")

try:
    person[0] = "John"
    print(person)
except Exception as e:
    print(f"Exception is: {e}")