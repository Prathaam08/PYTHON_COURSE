class Animals:
    def __init__(self , name , species):
        self.name = name 
        self.species = species
         

class Dog(Animals):
    def __init__(self, name , breed):
        super().__init__(name, species="Dog")
        self.breed = breed
    def makesound(self):
        print("Barks!!")

class Cat(Animals):
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.breed = breed
    def makesound(self):
        print("Meoww!!")

moti = Dog("moti" , "Doberman")
print(moti.name)
print(moti.breed)
print(moti.species)
moti.makesound()

mani = Cat("mani" , "street")
print(mani.name)
print(mani.breed)
print(mani.species)
mani.makesound()

        
        

