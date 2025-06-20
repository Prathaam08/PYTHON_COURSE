# MAP

# def square(x):
#     return x * x 

l = [ 1 , 2 , 3 , 4]

# newl = list(map(square , l))

#  using lambda function
newl = list(map(lambda x: x * x , l))
print(newl)

# FILTER
# def filter_number(a):
#     return a > 2

# newlist = list(filter(filter_number, l))

#  using lambda function
newlist = list(filter(lambda a: a > 2 , l))

print(newlist)

# REDUCE 

from functools import reduce

marks = [10 ,20 , 30]
sumlist = reduce(lambda x,y: x+y , marks)
print(sumlist)
