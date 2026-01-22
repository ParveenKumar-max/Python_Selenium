# Find common Element from list


List1 = [1,2,3,4,4,5]
List2 = [1,3,4,7,9,7]

Common_Element = list(set(List1) & set(List2))
print(f" Above line only prints Common Element", {Common_Element})
# set(List1) & set(List2) is the set intersection operator "&",
# which returns only the elements that are present in both sets; here that is [1, 3, 4]

Remove_Duplicate = list(set(List1) | set(List2))
print(f"Above line removes duplicat Element", {Remove_Duplicate})

# set(List1) | set(List2) is the set union operator "|",
# Returns a new set
# Contains unique elements from both lists
# Removes duplicates automatically here that is [1, 2, 3, 4, 5, 7, 9]
