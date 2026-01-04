# Duplicate element found in list


list = [1,1,2,3,3,4,4,5,6,]
seen = set()        #set() creates an empty set
duplicates = []     # Empty list
for items in list:
    if items in seen:
        if items not in duplicates:
            duplicates.append(items)
    else:
        seen.add(items)

print("Original list", list)
print("Found duplicate value", duplicates)
print("Element in Set", seen)

# list copy in items
# check element is present in seen or not, if not else loop will work, seen.add(items)
# check if element is found in seen, then duplicate loop will execute.
print("********************************************")

list1 = [1,1,2,3,3,4,4,5,6,7]
seen1 = set()        #set() creates an empty set
duplicates = []     # Empty list
for items in list1:
    if items not in seen1:
        if items not in duplicates:
            duplicates.append(items)
    else:
        seen1.add(items)

print("Original list", list1)
print("Found duplicate value", duplicates)
print("Element in Set", seen1)
# It won't print anything in seen1 because set is empty and the condition we add
# items not in seen1 is true everytime, so it won't execute seen.add(items block.)