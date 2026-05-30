print("***********************PYTHON BASICS****************************** \n ")
ex_var = 7
print(ex_var)
ex_var_second = 7.6
print(ex_var_second)
ex_var_third = True
print(ex_var_third)
ex_var = 9
print(ex_var + (10*90.123))


# Will divide all variables with 100, because price is in $ dollars

number_1 = 16.68 * 100
number_2  = 6.98 * 100
number_3 = 16.78 * 100
number_4 = 15.26 * 100
number_5 = 3.00 * 100
number_6 = 4.39 * 100
Sum_integer = (number_1 + number_2 + number_3 + number_4 + number_5 + number_6)
Sum_round = round(number_1 + number_2 + number_3 + number_4 + number_5 + number_6)
print(Sum_integer)
print(Sum_round)

print("***********************HOW TO WORK WITH INDEXING****************************** \n")
string_value = "Just Do it!"
print_i = string_value[8:9]
print(print_i)
print_do = string_value[5:7]
print(print_do)
print_it = string_value[8:10]
print(print_it)
print_just = string_value[0:5]
print(print_just)

concat = ("Don't" + string_value[5:10])
print(concat)

print("*******************HOW TO USE TYPES INPUT********************************** \n ")

var_one_more = 31.333
print(type(var_one_more))
var_two_more = str(31.333)
print("String", type(var_two_more))
print("\"Hello, I'm Parveen,\n it's nice to meet you!\"")



print("*******\n *****\n  ***\n   *")
print("   *\n  ***\n *****\n*******")

print("********************STRINGS********************************* \n")


value_input = int(input("Enter your name"))
sum = 10
print("My name is", value_input + sum) # it will give TypeError: can only concatenate str (not "int") to str
# Here it will gove error, because input returns type is always string, and we can't add string with integer, so we need to convert sum into string or value_input into integer,
#and you can't concatinate str + int
print(type(value_input))

name = input("What is your name?")
quest = input("What is your quest?")
color = input("What is your favorite color?")
 
print("So your name is " + name + ", \n your quest is " + quest + ", \n and your favorite color is " + color + ".")



print("********************FUNCTIONS********************************* \n")

def hello_world_printer():
    print("Hello World!")
hello_world_printer()

def name_printer(name):
    print("Hello", name)
name = input("What is your name ?")
name_printer(name)


length = int(input("Enter length"))
width = int(input("Enter width"))
height = int(input("Enter height"))

def volume_calculator(length, width, height):
    return length * width * height
    
print("The volume of the rectangular prism is " + str(volume_calculator(length, width, height)) + " cubic feet.")


print("********************Programming Knowledge********************************* \n")

# Celsius to Fahrenheit Solution with integers

celcius_temp = int(input("Enter an integer value in Celcius."))

def fahrenheit(cel):
    # To avoid the approximation error that would occur if the float 1.8 was used in the calculation, 1.8 * 10 is used
    # instead, resulting in the integer 18.  To balance this out, 32 is also multiplied by 10 to get 320.  After the
    # calculations in the parentheses are finished, the result is divided by 10, which gives the correct Fahrenheit
    # F = 1.8 * C + 32
    return 18 * cel + 320 / 10

print("The Fahrenheit equivalent of", str(celcius_temp), "degrees Celsius is", str(fahrenheit(celcius_temp)), "degrees Fahrenheit.")

# Celsius to Fahrenheit Solution with round()

celsius = int(input("Please enter an integer value for degrees celsius. "))
 
 
def fahrenheit(cel):
    # The second argument of round() is 1 since we only want the Fahrenheit temperature to be displayed with 1 number
    # after the decimal point
    return round((1.8 * cel + 32), 1)
 
 
print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")

print("********************Programming Knowledge 2 ********************************* \n")



# Miles Per Gallon Solution with random integers

from random import randint
# generates random integer between and inclusive of 10 and 25 to represent gas in the car's fuel tank
fuel = randint(10, 25)
# generates random integer between and inclusive of 200 and 400 to represent miles the car can go without refueling
miles = randint(200, 400)
# calculates and displays the MPG of the car assuming car manufacturers overestimates in their claims
print("The car can travel " + str(miles // fuel) + " miles per gallon.")
# displays the number of gallons of fuel that the car's fuel tank can hold
print("The car's fuel tank can hold " + str(fuel) + " gallons.")
# displays the number of miles that the car can travel on a full tank
print("The car can travel " + str(miles) + " miles on a full tank.")




