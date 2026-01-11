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

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

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


def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)   # *args is  positional argument and **kwargs is Keyword Argument
        return wrapper
    return decorator


@repeat(3)
def say_hi():
    print("Hi")


say_hi()

# repeat(times)        ← decorator with argument
#  └── decorator(func)  ← actual decorator
#      └── wrapper()    ← wraps the target function