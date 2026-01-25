# Count Digit, Space, and alphanumeric in given letter

value = input("Enter any numbers :")
digit = 0
space = 0
alpha = 0
for text in value:
    if text.isdigit():
        digit = digit + 1
    elif text.isspace():
        space = space + 1
    elif text.isalpha():
        alpha = alpha + 1

print(f"Digit is: {digit}, Space is {space}, letter is {alpha}")
