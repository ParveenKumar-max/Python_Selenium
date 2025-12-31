# Duplicate element found in list


list = [1,1,2,2,3,3,4,4,5,5,6,6]
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

# list copy in items
# check element is present in seen or not, if not else loop will work, seen.add(items)
# check if element is found in seen, then duplicate loop will execute.