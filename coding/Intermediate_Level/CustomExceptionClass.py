#CustomExceptionClass --> We will create a Exception class

class customeException(Exception):
    pass                            # once we create a class of exception, we will by-default pass it

def customMethod(value):
    if value % 2 == 0:
        raise customeException("Call customException class")
    print(f"Result successfully shown: {value}")

try:
    my_value = int(input("Enter any number :"))
    custom_value = customMethod(my_value)
    print(custom_value)
except customeException as e:
    print(f" Handle Exception via class {e}")
