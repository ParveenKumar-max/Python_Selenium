# Long Value in sentence

value = input("Find Long value from Sentence: ")

word = value.split()
count_long = max(word, key=len)

print(f"Found long value in sentence is: {count_long}")

# Largest Number in the list

list = [12,45,48,123,46,789,999,1023,1456,1456,7893]
largest_list = max(list)
print(f"Largest number from given 'List' {list} is {largest_list}")

# Second way to find largest number

list1 = [10,2,3,4,5,6,7,8,9,90]
largest = list1[0]
for value in list1:
    if value > largest:
        largest = value
print(f"Largest value is: {largest}")

# Third way to get the element via sort

list2 = [22,33,44,55,66,77,88,99,100]
largest1 = sorted(list2)
value1 = largest1[-1]
print(f"Largest value via sort is: {value1}")


