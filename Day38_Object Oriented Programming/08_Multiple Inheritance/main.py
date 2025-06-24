class Employee:
    def __init__(self,name , id):
        self.name =  id
    def showName(self):
        print(f"The name is {self.name}")

class dancer:
    def __init__(self , dance):
        self.dance = dance

class dancerEmployee(Employee , dancer):
    def __init__(self , name , dance ):
        self.name = name
        self.dance = dance
    def showDance(self):
        print(f"The name is {self.dance}")


employee1 = dancerEmployee("Pratham" ,"Breakdance")
print(employee1.name)
print(employee1.dance)
employee1.showName()
employee1.showDance()