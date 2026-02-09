#Parent class of inheritance


from Python_TestScripts.PythonBasicwithOops_Level1.Python_inheritance_Base import BaseConstructor


class ParentConstructor(BaseConstructor):
    var_num2 = 200

    def __init__(self):             #instead of using BaseConstructor name , we can use SUPER keyword.
        super().__init__(10, 20, 30)

    def ParentMethod(self):
        total_amount = self.adding_values()
        return f"Final Value: {total_amount + self.var_num2}"

object_parent = ParentConstructor()
print(f"Value of Parent or Small class, {object_parent.ParentMethod()}")
object_base = BaseConstructor(1,2,3)
print(f"Value of Base or Big class, {object_base.adding_values()}")
