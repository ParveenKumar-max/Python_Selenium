# Handle multiple Exception

list_all = ['a',123, 456, 'qwerty'] # mixed list of integer and string

try:
    total = list_all[1] + list_all[2] # we can add list_add[3], it will goto except part
    print(f"Value Added, {total}")
except (ValueError, TypeError) as e:
    print(f"Total value isn't added because of incorrect data")
except:
    print("Out of range")
finally:
    print("Thanks")

# Handle Exception

try:
    # Code that might cause an error goes here
    numerator = 10
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
    print(f"The result is: {result}")

except ZeroDivisionError:
    # This runs if the user enters 0
    print("Error: Cannot divide by zero!")

except ValueError:
    # This runs if the user enters something that is not a valid integer (like text)
    print("Error: Please enter a valid integer.")

else:
    # This runs ONLY if the 'try' block succeeded without any errors
    print("Division successful (no exceptions raised).")

finally:
    # This runs regardless of whether an error occurred or not
    print("Execution finished. Cleanup complete.")