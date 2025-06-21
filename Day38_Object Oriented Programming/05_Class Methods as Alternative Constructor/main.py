class employee:
    def __init__(self,name , salary):
        self.name = name
        self.salary = salary
    
    # using this we can handle different input 
    # @classmethod
    # def forString(cls,string):
    #     return cls(string.split("-")[0] , string.split("-")[1])
    

    # suppose if there is * in middle 
    @classmethod
    def forString(cls,string):
        return cls(string.split("*")[0] , string.split("*")[1])
    

emp1 = employee("Pratham" , 500)
print(emp1.name)
print(emp1.salary)

# string = "pratham-600"
# emp2 = employee.forString(string)
# print(emp2.name)
# print(emp2.salary)

string = "pratham*60000"
emp3 = employee.forString(string)
print(emp3.name)
print(emp3.salary)
        


