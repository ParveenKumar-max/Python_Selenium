import copy

# Original List with nested list. You can only append the nested list not main list content.
# Because if you append the main list, it wil add the element at the last.
shallow_copy_list = [1,2,[3,4],6,7]

# Copy original list to another via shallow copy
copy_shallow_list = copy.copy(shallow_copy_list)
copy_shallow_list.append(7)
copy_shallow_list[2].append(5)

print(f"Original List : {shallow_copy_list}")
print(f"Copy & Add element in shallow List : {copy_shallow_list}")

print(f"************Updating the Shallow list********")

copy_shallow_list[1] = 9

print(f"Original List : {shallow_copy_list}")
print(f"Copy & Add element in shallow List : {copy_shallow_list}")

# As you can see in the output, the main list is also changed.


# Deep Copy Example

deep_copy_list = [10,20,[30,40],60,70]

# Copy original list to another via shallow copy
copy_deep_list = copy.deepcopy(deep_copy_list)
copy_deep_list.append(70)
copy_deep_list[2].append(50)

print(f"Original List : {deep_copy_list}")
print(f"Copy & Add element in shallow List : {copy_deep_list}")

print(f"************Updating the Deep list********")

copy_shallow_list[1] = 9

print(f"Original List : {deep_copy_list}")
print(f"Copy & Add element in shallow List : {copy_deep_list}")

# As you can see in the output, the main list isn't changed.