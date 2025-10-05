# Try Catch --> Try Catch we use to handle the exception and print the user expected result.


try:
    file = open('TestFile1.txt')
    line = file.read()
    print(line)
except Exception as e:
    print("File Not Found", e)
finally:
    print("ThankYou for learning Try Catch")
