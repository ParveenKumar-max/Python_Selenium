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
    print("The number is out of range")