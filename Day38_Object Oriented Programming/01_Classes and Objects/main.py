class person:
    name = "Pratham"
    occupation = "Python Developer"
    age = 21
    salary = 100
    # self parameter is a reference to the current instance of thr class and it is used to access variable that belongs to the class
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
print(a.name)
a.info()

# To change the values 
a.name = "Shawn"
print(a.name)

a.info()