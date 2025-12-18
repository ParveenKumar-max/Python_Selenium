# Read and Write the file

#r	Read only, r+	Read + Write, w	Write (overwrite), a	Append, a+	Read + Append
try:
    file_r= "D:/Read_Write.txt"
    with open(file_r, "r") as f:
        content = f.read()
        print(f"Read Full file in full go: {content}")
        f.seek(0)
        content1 = f.readline()
        print(f"Read file line by line: {content1}")
# The reason it's showing blank, after reading full content, cursor reaches to end, and cursor has noting to read.
# So make it up, we have use seek(), it moves the cursor at start point.

except Exception as e:
    print("File", e)

# Write the content in the file

file_w = "D:/Read_Write.txt"
with open(file_w, "w") as f1:
        content2 = f1.write("Write any number 123456")
        print(f"Content added, {content2}")


