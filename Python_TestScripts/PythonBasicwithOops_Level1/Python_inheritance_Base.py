# Inheritance  means --> Always works in two classes. Base class can fetch or bring all the methods and variables from
# parent class, Other programming language we use Keyword EXTENDS, But in Python, we declare it in different way.


class BaseConstructor():
    var_num1 = 100

    def __init__(self, a, b, c):
        self.value1 = a
        self.value2 = b
        self.value3 = c

    def value(self):
        return("Creating one return type method")

    def adding_values(self):
      #  return f"Adding all the values: {self.value1 + self.value2 + self.value3 + self.var_num1}" #Adding all the values: 274
        amount_verified =  (self.value1 + self.value2 + self.value3 + self.var_num1) #('Adding all the values', 274)
        return amount_verified


object_value = BaseConstructor(20, 60, 30)
print(object_value.value())
total_amount_verified = object_value.adding_values()
print("Total Amount Verified : " , total_amount_verified)

