# While loop condition
print("While loop Program and conditions")

a = 1
b = 0
while a <= 5:
    b = b + a
    if b != 15:  # We add one more condition here,
        print(b)
    a = a + 1   # If we didn't add last condition a = a +1, then the program will run in infinite loop.



c = int(input("Want to add Integer"))
d = 0
while c <= 5:
    d = d + c
    if  d != 5:
        print("Value is greater than : ", d)
    elif d in (6, 10) :
        print("Value is equal to tuple: ", d)
    elif d != 3:
        print("Value is not equal to: ", d)
    elif d % 2 == 0:
        print("Value of Mod is: ", d)
    else:
        print("Wrong input")
c = c + 1

e = int(input("Want to add Integer"))
f = 0
while e >= 0:
    f = f + e
    if  f != 15:
        print("Value of f is :", f)
    e =  e - 1

print("Value is greater than : ", e)