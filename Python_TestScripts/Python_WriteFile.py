# Write the content in the file
# For writing we have function like

with open('TestFile.txt', 'r') as reader:       #'r' we have to mentioned it, we are reading the content in the file
    content = reader.readlines()                # Read the whole content in the file
    reverse_value = list(reversed(content))     # reversed function, reverse the whole file content and stored it in variable
    # Convert reversed iterator into list
    for all_line in reverse_value:
        print(all_line, end="")              # avoid extra blank line because line already contains new line /n

with open('TestReversedFile.txt', 'w') as writer:       #'w' we have to mentioned it, we are writing the content in the file
            for line in reverse_value:
                writer.write(line)
                print(line, end="")

print("\n\n✅ Reversed content has been written into 'TestFile_Reversed.txt'")