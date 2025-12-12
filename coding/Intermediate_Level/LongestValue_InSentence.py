# Long Value in sentence

value = input("Find Long value from Sentence: ")

word = value.split()
count_long = max(word, key=len)

print(f"Found long value in sentence is: {count_long}")