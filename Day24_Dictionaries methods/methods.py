dic = {
    'name' : 'pratham',
    'age' : 20
}

dic2 = {
    'id' : 255,
    'salary' : "1L"
}

dic.update(dic2)
print(dic)

# clear()
print(dic.clear())

#pop() 
dic3 = {
    'product' : 'candy',
    'price' : 100,
    'manufacture' : 'cadbury'
}
dic3.pop('price')
print(dic3)

# popitem() : It will remove the last key-value pair from the dictionary
dic3.popitem()
print(dic3)

# del
# del dic3

# del dic3['product']









