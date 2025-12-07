# create a pyramid

num = 5
for i in range ( 1, num + 1):
    print( "  " * (num -i) + "*" * (2 * i - 1))

# Line-by-line explanation
# num = 5

# for i in range ( 1, num + 1):
# Creates a loop where i goes from 1 to 5 (inclusive).
# Each value of i represents the current row number being printed.
# print( " " * (num - i) + "*" * (2 * i - 1))
# " " * (num - i) creates leading spaces so the stars are centered.
# On row 1: num - i = 4 spaces
# Row 2: 3 spaces, …, row 5: 0 spaces. and so on.
# "*" * (2 * i - 1) creates the stars for that row.
# Row 1: 2*1 - 1 = 1 star
# Row 2: 2*2 - 1 = 3 stars
# Row 3: 5 stars, row 4: 7 stars, row 5: 9 stars.
# The + concatenates spaces and stars into one string for that row,
# which print outputs on its own line.