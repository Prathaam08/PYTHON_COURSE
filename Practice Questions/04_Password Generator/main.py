import string 
import random

s1 = string.ascii_uppercase
s2 = string.ascii_lowercase
s3 = string.digits
s4 = string.punctuation

passwordLen = int(input("Enter the length of password: "))

s = []

s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

random.shuffle(s)
print("".join(s[0:passwordLen]))