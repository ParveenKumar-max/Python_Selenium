# class is a blueprint or prototype,
# Also we can say, it's the combination of variable(Property) and Method(Behaviour).

class calculator:                   # Calculator is a class
    num = 100

    #Define Constructor

    def getData(self):                      # Method getData
        print("I'm Parveen Chaudhary. Want to be Sn. Tech Lead of Automation ")

object_Creation = calculator()  # Object create in python.
object_Creation.getData()
print(object_Creation.num)