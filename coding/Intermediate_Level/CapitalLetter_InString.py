# Capital Letter in String

value = input("Enter Nay Numbers: ")
sums = 0
for i in value:
    if i.isupper():
        sums = sums + 1
        print("The upper chars are :", i)
print("Value in Upper:", value, "is", sums)