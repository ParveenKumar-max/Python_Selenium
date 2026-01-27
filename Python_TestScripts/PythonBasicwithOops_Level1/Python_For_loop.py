# For loop condition

value_list = [12,34,45,56,67,78,89,90]
for length in value_list:
    print(length)

print("Value in for loop printed", length)

# Want to count length

counting = 0
for length_count in value_list:
    print("Length of list : ", length_count)
    counting = counting + length_count
print("Adding of value_list is : ", counting)


# Range we will use when we want to count from 1 to 9 like (1,2,3,4,5,6,7,8,9,10)
for summation in range(12,34):
    counting = counting + summation
print("Value of summation is :", counting)

for k in range(1,10,8):
    print(k)