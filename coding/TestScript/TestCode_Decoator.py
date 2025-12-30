# Python Decorator
# A decorator in Python is a special function that:
#
# Adds extra behavior to another function
#
# Without changing the original function’s code


# Decorator without Syntax
def MyDecorator(func):
    def MyTest():
        print("Before MyTest Function")
        func()
        print("Main Function")
    return MyTest

def MyAfterTest():
    print("After Main Function")

MyAfterTest = MyDecorator(MyAfterTest)
MyAfterTest()

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# Decorator with Syntax
def MyDecorator(func):
    def MyTest():
        print("Before MyTest Function")
        func()
        print("Main Function")
    return MyTest
@MyDecorator
def MyAfterTest():
    print("After Main Function")

MyAfterTest()

# With the help of decorator, we can hide the main function functionality.