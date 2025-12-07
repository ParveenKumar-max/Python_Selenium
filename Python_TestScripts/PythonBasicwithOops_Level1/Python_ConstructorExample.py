class BasicCalculator():
    def __init__(self, a , b):
        self.firstNumber = a
        self.secondNumber = b
        #print("Automatically called when create an instance of the class.")
        #
    def getAddition(self):
        return self.firstNumber + self.secondNumber



    def getSubtraction(self):
        return self.firstNumber - self.secondNumber


    def getMultiplication(self):
        return self.firstNumber * self.secondNumber

    def getDivision(self):
            return self.firstNumber / self.secondNumber

object_Value = BasicCalculator(10, 5)
result_addition = object_Value.getAddition()
print(f"Addition: {object_Value.firstNumber} + {object_Value.secondNumber} = {result_addition}")

result_Subtraction = object_Value.getSubtraction()
print(f"Subtraction: {object_Value.firstNumber} - {object_Value.secondNumber} = {result_Subtraction}")

result_Multiplication = object_Value.getMultiplication()
print(f"Multiplication: {object_Value.firstNumber} * {object_Value.secondNumber} = {result_Multiplication}")

result_Division = object_Value.getDivision()
print(f"Division: {object_Value.firstNumber} / {object_Value.secondNumber} = {result_Division}")