# cHECK HOW MANY Capital Letter in THE String

value = input("Enter Any Numbers: ")
sums = 0
for i in value:
    if i.isupper():
        sums = sums + 1
        print("The upper chars are :", i)
print("Value in UpperCase:", value, "is", sums)