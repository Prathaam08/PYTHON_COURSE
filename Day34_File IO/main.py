# r for reading , w for writing , a for appending , rb for image , pdf etc

f = open('File IO/myfile.txt' , 'r')
text = f.read()
print(text)
f.close()

# w this mode open the file for writing only and creates a new file if doesn't exists
f = open('File IO/myfile1.txt' , 'w')
f.write('Helloo again')
f.close()

# this mode open the file for appending only and creates a new file if doesn't exists

f = open('File IO/myfile1.txt' , 'a')
f.write('again hello')
f.close()

# using 'with' the file will automatically close
with open('File IO/myfile2.txt' ,'a') as f:
    f.write("Hey Hello")

# readline() method

f = open('File IO/myfile3.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

# seek() method allowa you to move the cuirrent position within the file to a specific points.

# tell() will tell the seek position value

with open('File IO/myfile4.txt' ,'r') as f:
    print(f.read())
    f.seek(10)
    print(f.tell())
    data = f.read(5)
    print(data)
