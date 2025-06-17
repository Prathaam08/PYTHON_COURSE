dic = {
    'name' : 'pratham',
    'age' : 20
}
print(dic)
# It will throw error if the key is not present
print(dic['age'])

# It will not throw error if the key is not present
print(dic.get('gg'))

print(dic.keys())
print(dic.values())
print(dic.items())
