x = [1 , 2 , 3]

print(dir(x))  # It will print all the methods for the list

# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# If you want to info about particular method then
print(x.__add__)

class person:
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id 

person1 = person("pratham" , 20 , 49)
print(person1.name)
print(person1.__dict__)  # it will print all the object attribute in dictionary

print(help(person))
