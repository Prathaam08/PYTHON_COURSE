# Union and union update 
s1 = { 2 , 4 , 8 ,1 , 10}
s2 = { 12 , 14 , 10 }
print(s1.union(s2))

# update will update the s1 set with the union of s1 and s2
s1.update(s2) 
print(s1)

# intersection and intersection_update()
cities = {"mumbai" , "thane" , "kolkatta" , "pune"}
cities2 = {"bangolare" , "nashik" , "mumbai"}
cities3 = cities.intersection(cities2)
print(cities3)

# intersection_update() will update the cities set with intersection of cities and cities2
cities.intersection_update(cities2)
print(cities)

# symmetric difference and symmetric_difference_update() 
# It prints the value that are not common
country = {"india" , "china" ,"america" , "japan"}
country2 = {"russia" , "japan", "america" , "england"}
country3 = country.symmetric_difference(country2)
print(country3)

country.symmetric_difference_update(country2)
print(country)

# isdisjoint() : This method return False if items are present in another set else True
animal = {'dog' , 'cat' , 'lion'}
animal2 = {'dog' , 'tiger' ,'monkey'}
animal3 = animal.isdisjoint(animal2)
print(animal3)

# issuperset() : It checks if all the items of a particular set are present in the original set if present it return True else False
num = {1 ,2 , 4 ,5}
num2 = {2 , 4}
print(num.issuperset(num2))

# issubset() : It checks if all the items of original set are present in particular set if present return True else False
print(num2.issubset(num))

# add()
num.add(100)
print(num)

# remove() : It will throw error if the value is not present 
num.remove(100)
print(num)

# discard() : It will not throw the error if the value is not present 
num.discard(180)
print(num)

# del : It will delete the sets
apps = {'google' , 'insta'}
del apps

# clear() : It will remove all the value in set
apps1 = {'google' , 'insta'}
print(apps1.clear()) 