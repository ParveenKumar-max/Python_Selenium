# Constructor is a special type of method, which have same name as the class name. Constructor has no return type.
# Constructor automatically invokes when we create an object.

# class is a blueprint or prototype,
# Also we can say, it's the combination of variable(Property) and Method(Behaviour).

class calculator:                   # Calculator is a class
    num = 100

    #Define Constructor
    def __init__(self, a, b):
        self.firstValue = a
        self.secondValue = b
        print("I'm called automatically when object is created.")

    def getData(self):                      # Method getData
        print("I'm Parveen Chaudhary. Want to be Sn. Tech Lead of Automation ")

    def summation(self):            # Method where we call instance variable and class variable
        return self.firstValue + self.secondValue + self.num

object_Creation = calculator(5, 7)  # Object create in python. Creating instance variable.
object_Creation.getData()
print(object_Creation.summation())


object_Creation1 = calculator(10, 20)  # Object create in python. Creating instance variable.
object_Creation1.getData()
print(object_Creation1.summation())