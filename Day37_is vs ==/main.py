# here 4 is immutable , constant so python will not assigned another memory for 4 
a = 4   
b = 4

print(a is b)   # is find exact location of object in memory 
print(a == b)   # == compare values

# For List i will return false 
c = [ 1 , 2 , 3]
d = [ 1 , 2 , 3]

print(c is d)   # is find exact location of object in memory 
print(c == d)   # == compare values

