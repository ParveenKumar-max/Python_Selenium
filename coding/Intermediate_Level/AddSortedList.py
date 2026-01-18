# Create two list and merged it and sort it

list_one = [1,3,5,6,7,9]
list_two = [2,4,6,8,10]

list_three = sorted(list_one + list_two)
list_four = list(list_one + list_two)
list_five = set(list_one + list_two)


print("Sorted with added both list values are: ", list_three)
print("Only merged both list values are: ", list_four)
print(f"Merged both list but remove duplicate: {list_five}")
