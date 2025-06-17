marks = [ 75 , 75 , 44 , 22, 25 , 88 , 99]
print(marks)

print(marks.index(25))
print(marks.count(75))

marks.insert(1 , 50)
print(marks)

marks2 = [ 500 , 200 ,300]
marks.extend(marks2)

marks.append(100)
print(marks)

marks.reverse()
print(marks)

marks.sort()
print(marks)

marks.sort(reverse=True)
print(marks)

