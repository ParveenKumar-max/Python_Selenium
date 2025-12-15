# Two sum problems

# The Two Sum problem asks, you to find two numbers in an array whose sum equals a given target,
# and return their indices.
#Defines a function that takes:

#nums → list of numbers
#target → required sum

# for i, num in enumerate(nums):
# Loops through the list:
#


def two_sum(nums, target):
    seen = {}   # empty dictionary

    for i, num in enumerate(nums):
# i → index , num → value at that index
        complement = target - num

        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

nums = [2,7,11,15]
target = 26

result = two_sum(nums, target)
print(result)