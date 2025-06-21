class employee:
    def __init__(self , name , id):
        self.name = name
        self.id = id

    def showDetail(self):
        print(f"The id {self.id} belongs to {self.name}")

class which_department(employee):
    def __init__(self, name, id , department):
        super().__init__(name, id)
        self.department = department
    def showDepartment(self):
        print(f"The name of department is {self.department}")

employee1 = employee("Pratham" , 39)
employee1.showDetail()

employee2 = which_department( "Kalpesh" , 49 ,"software" )
employee2.showDetail()
employee2.showDepartment()

