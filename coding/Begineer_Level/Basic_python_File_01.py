print("********************Variables********************************* \n")

global_var_one = 30
global_var_two = "Var_3"

print("Global variables before calling functions:", global_var_one, global_var_two)

def local_scope_example(var_one, var_two):          # var_one and var_two are local inside this function
    var_one = 10
    var_two = "Var_1"
    return var_one, var_two

print("Local function returned:", local_scope_example(global_var_one, global_var_two))
print("Global variables after local function call:", global_var_one, global_var_two)


def global_scope_example():
    global global_var_one, global_var_two
    global_var_one = 20
    global_var_two = "Var_2"
    return global_var_one, global_var_two

print("Global function returned:", global_scope_example())
print("Global variables after global function call:", global_var_one, global_var_two)

print("******************** If ELSE wth Random import functions********************************* \n")

# Roman Numeral Equivalent Solution - Program
from random import randint
Random_number = randint(1, 10)

if Random_number == 1:
    print("The roman numeral equivalent of " + str(Random_number) + " is I")
elif Random_number == 2:
    print("The roman numeral equivalent of " + str(Random_number) + " is II")  
elif Random_number == 3:
    print("The roman numeral equivalent of " + str(Random_number) + " is III")
elif Random_number == 4:
    print("The roman numeral equivalent of " + str(Random_number) + " is IV")
elif Random_number == 5:
    print("The roman numeral equivalent of " + str(Random_number) + " is V")
elif Random_number == 6:
    print("The roman numeral equivalent of " + str(Random_number) + " is VI")
elif Random_number == 7:
    print("The roman numeral equivalent of " + str(Random_number) + " is VII")
elif Random_number == 8:
    print("The roman numeral equivalent of " + str(Random_number) + " is VIII")
elif Random_number == 9:
    print("The roman numeral equivalent of " + str(Random_number) + " is IX")
elif Random_number == 10:
    print("The roman numeral equivalent of " + str(Random_number) + " is X")
else:
    print("The number is out of range \n")


print("********************Intro Of Loops********************************* \n ")

print(" *******************While Loop**************************************")

while_loop = 10
while while_loop > 0:
    print(while_loop)
    while_loop -= 1

# For while loop, you always need exist point, if you didn't use, the program will run in infinite loop.

sum_of_while = input("Enter a number to find out the sum of numbers..")
int_value1 = int(sum_of_while)
sum = 0
while int_value1 > 0:
    sum = sum + int_value1  # This line is used to add the numbers
    int_value1 -= 1         # This line is used to decrease the value of int_value1 by 1 in each iteration, so that the loop can eventually terminate when int_value1 becomes 0 or negative.
print("The sum of numbers from 1 to " + sum_of_while + " is " + str(sum))


print(" *********************** for loop *******************")

letter = "Hello Pareen !"
for word in letter:
    print(word)


# Find The Number of Characters in A String

one_string = input("Enter a string to find out the number of characters in it..")
count = 0
for char in one_string:
    count = count + 1
print("The number of Enter the sting is. " + str(one_string))
print("The number of character in the string is ", + (count))


print(" *********************** RANGE *******************")

one_range = range(11,16)
for num in one_range:
    print(num)

# Programming Challenge: Fizz Buzz
print("********************Fizz Buzz********************************* \n")


for num in range (1 , 10):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

def fact(value):
    if value == 0 or value == 1:
        return 1
    else:
        return value * fact(value - 1)
print("The factorial of 5 is " + str(fact(5)))

def fact_two(value2):
    result = 1

    for num in range (value2, 1, -1):
        result = result * num
    return result
print("The factorial of 2 is " + str(fact_two(2)))

print("******************** String Function ********************************* \n")

mixed_case = ("A Song of Ice and Fire".isupper())
print(mixed_case)