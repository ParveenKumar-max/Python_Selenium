# Working with while loop

a = 10
b = 0
while a >=0 :
    if a == 7:
        a = a - 1
        continue        # Continue keywords skip the current iteration in the program.
    print("Value of a is : ", a)
    if a == 5: # Break condition only work when it matches the exact value, until then it runs.
        break  # It won't print anything after 5, because we halt the execution using BREAK condition.
    print("Value of a matching with: " , a)
    a = a - 1
print("Program ends")