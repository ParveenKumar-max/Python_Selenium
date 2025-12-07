# count vowels from string

# two ways to find out the vowels

values = input("Enter the String : ")
vowels = "aeiouAEIOU"
count = 0

for text in values:       # text will fetch the every single char from full string.
    if text in vowels:
        count += 1
# count += 1 means “increase the value of count by 1 and store it back in count.”​

# It is shorthand for count = count + 1.

print("Find or count the vowels",  count)


def values(number):
    vowels = "aeiouAEIOUD"
    return sum(1 for ch in number if ch in vowels)


# Sum is also a predefined function sum( __iterable, start)

user_input = input("Enter the string : ")
print("Numbers of vowels ", values(user_input))