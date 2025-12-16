# You can count the occurrences of an element in a list in Python using the built-in
# list.count() method, a manual loop, or the collections.Counter class.
from collections import Counter

# Means Element 1 appear 3 times in a list

list = [1,1,2,3,3,4,4,5,6]

element_to_count = 3

my_list = list.count(element_to_count)  # Want to count 3 from list

print(f"The value {element_to_count} appears in {my_list} times in list")

# 2nd way for loop

count = 0
for i in list:
    if i == element_to_count:
        count = count + 1
print(f"Value appear {count} time in list")

# 3rd way collection.counter

list1 = ['apple', 'apple', 'kiwi', 'kiwi', 'banana', 'orange', 'pineapple']

find_element_occurrence = Counter(list1)
print(find_element_occurrence.items())

print(f"'apple' appears {find_element_occurrence['apple']} times in list1")

