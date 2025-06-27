# It genrates the values on the fly instead of storing

def my_generartor():
    for i in range(500):
        yield i

gen = my_generartor()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
