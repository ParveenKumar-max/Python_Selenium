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
print(object_parent.ParentMethod())
