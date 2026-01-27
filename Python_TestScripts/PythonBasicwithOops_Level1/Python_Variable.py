a = 5 # create variable a and print it
b = 10
c = "Parveen"
pi = 3.1415926535

print(a , b, c)  # it will give you an error
print(a + b)    # it will add both the variable
print(c)        # It will print Parveen
print(type(a))      # It will show a which datatype of variable. Output <class 'int'>
print(type(pi))      # It will show a which datatype of variable. Output <class 'floating'>
print("Value of function is", a,"&", c)     # it will give Value of function is 5 Parveen
print("Print the value {:.3}".format(pi)) # It will print only 2 places of decimal



ab, bc, de, ef, gh = 5,6,7,"Parveen","Kumar"
print(type(ef))
print("Value of both variables is int & str: ",ab, ef)
print("Value of function is str & str", ef +" " ,gh) # String you can concatenate with +

## Want to concatenate int + String, you have to use format function. Like below
print("{} {}".format("Value is", ef))

age, height, color = 25, 5.8, "blue"
print("Age is:", age, " | Type is", type(age), " | Height is : " ,height, " | Color is", color)


print("My Age is :{} and My favourite color is :{}".format(ab, ef) )
print(f"My Age is: {age} and My favourite color is : {color}")

