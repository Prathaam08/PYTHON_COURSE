import math 

result = math.sqrt(64)
print(result)

# If you want to use particular module 

from math import sqrt , pi
result = math.sqrt(64) * pi
print(result)

# You can also give custom name to modules 

# import math as m

from math import sqrt as s 
result = s(64)
print(result)

from greet import greet , dog
greet()
print(dog)