class Employee:
    company = "Apple"

    def show(self , name ):
        self.name = name
        print(f"The name of the employye is {self.name} and company name is {self.company}")

    # Company name is class method it will not chnage , If you want to change the company name @classmethod we need to use and first argument should always be "cls"
    @classmethod
    def changeCompany (cls , newCompany):
        cls.company = newCompany

emp1 = Employee()
emp1.show("Pratham")
emp1.changeCompany("Tesla")
emp1.show("Pratham")

