# print vowels from string

values = input("Enter the string: ")
vowels = "aeiouAEIOU"

for text in values:
    if text in vowels:
        print("Print vowels", text)