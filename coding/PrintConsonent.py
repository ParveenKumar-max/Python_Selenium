# Print consonent

values = input("Enter the String : ")
vowels = "aeiouAEIOU"
consonent = ""

for text in  values:
    if text not in vowels:
        consonent = consonent + text

print("Print all consonent", consonent)