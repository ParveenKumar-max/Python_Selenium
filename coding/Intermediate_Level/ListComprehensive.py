# List Comprehensive --> It is a concise way to create lists using an
# expression, loop, and optional condition in a single line.

val_list = [2,3,4,5,8]
val_rest = [i ** 2 for i in val_list]

print(f"Value of List {val_list} Comprehensive is : {val_rest}")

# For loop vs List Comprehensive

val_list1 = [3,4,5,6,7]
var_for = []
for num in val_list1:
    inum = num * 2
    var_for.append(inum)
print(f"value of for loop are : {var_for}")

# Conditional Statement

var_list2 = [1,3,5,7,9, 12]
var_condition = [num1 for num1 in var_list2 if num1 % 2 == 0]
print(f"Conditional List Comprehensive values are: {var_condition}")