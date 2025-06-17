# Tuples are immutable means we dont change it 

tup = ( 0, 15 , 55)
print(type(tup), tup )

# if we want to change,remove,add item of tuple so first we need to convert it into list 

countries = ( "India" , "Pakistan" , "China")

temp = list(countries)
temp.append("Russia")
print(temp)

temp.pop(1)
print(temp)

temp[1] = "Japan"
print(temp)

countries = tuple(temp)
print(countries)