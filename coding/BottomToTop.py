# Create a Right Pyramid

num = 10
for i in range( num , 0 , -1):
# range(start, stop, step) here means:
# start from num (10), go down to (but not including) 0, decreasing by 1 each time (-1).
    print( " " * (num -i) + "*" * (2 * i - 1))