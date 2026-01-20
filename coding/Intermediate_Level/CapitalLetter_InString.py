# CHECK HOW MANY Capital Letter in THE String

value = input("Enter Any Numbers: ")
sums = 0   # Create a integer variable
for i in value:
    if i.isupper():
        sums = sums + 1
        print("The upper chars are :", i)
    else:
        print("The lower case value is :", i)
print("Value in UpperCase:", value, "is", sums)