# create a Reverse Number

# First way to reverse the number, I think it's the best way to reverse the number or character.

Input_reverse = input("Enter the numbers : ")
char_set = ""
for i in Input_reverse:
    char_set = i + char_set
print(f"Actual number is: {Input_reverse} and the reverse number is: {char_set}")



# Second way to reverse the number,

num = int(input("Enter the number : "))
# input() is predefine function for taking input from user as str. So we type Cast it. ( int )

temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print("The given number is {} and reverse number is {}".format(temp, reverse))

# Third way to reverse the number

def My_number_reverse(number):
    return number[: : -1]

My_Entry = input("Enter any Number : ")
My_Reversed_number = My_number_reverse(My_Entry)
print(f"Actual number is: {My_Entry} and the reverse number is: {My_Reversed_number}")


# 1. Initial setup
# num = 123456
#
# Stores the original number whose digits will be reversed.
#
# temp = num
#
# Copies 123456 into temp.
#
# After the loop, num will become 0, but temp still keeps the original value
# if you want to print something like “original vs reversed”.
#
# reverse = 0
#
# This variable will gradually be built up into the reversed number.
#
# Starts at 0 because no digits have been processed yet.
#
# 2. Loop condition
# while num > 0:
#
# Keeps running as long as num is not zero.
#
# Each loop removes one digit from the end of num.
#
# For 123456, the loop will run 6 times (once per digit).
#
# Below is what happens in every iteration.
#
# First iteration
# Current values at the start:
# num = 123456, reverse = 0
#
# remainder = num % 10
#
# 123456 % 10 gives the last digit: 6.
#
# So remainder = 6.
#
# reverse = (reverse * 10) + remainder
#
# reverse was 0.
#
# reverse * 10 is 0.
#
# 0 + 6 = 6, so reverse becomes 6.
#
# Right now, reversed number (from processed digits) is 6.
#
# num = num // 10
#
# Integer division by 10 removes the last digit.
#
# 123456 // 10 = 12345.
#
# So num becomes 12345.