class person:
    def __init__(self , name , occupation):
        print("Hello")
        self.name = name
        self.occupation = occupation
    def info(self):
        print(f"{self.name} is a {self.occupation}")

person1 = person("Pratham" , "Python Developer")
person1.info()

person2 = person("Shawn" , "Java Developer")
person2.info()
