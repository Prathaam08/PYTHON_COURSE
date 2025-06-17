a = "Pratham!!!!!!!!!!"
print(len(a))

#strings are immutable
print(a.upper())
print(a.lower())

# rstrip() to trim the retreviing letters 
print(a.rstrip("!"))

# replace() To replace the word 
print(a.replace("Pratham","More"))

# Split() it is used to split the given string into list 
msg = " Hii Pratham!!, How are you"
print(msg.split(" "))

# Capitalize() it is used to make the first letter captical
heading = "future is here"
print(heading.capitalize())

heading1 = "python CoUrSe"
print(heading1.capitalize())


# center() it is used to align the string to the center as per the parameter given by the user
heading3 = "World is yours"
print(heading3.center(50))

# count() used to count the number of times given value occured in the string 
msg2 = "hello, hello who are you"
print(msg2.count("hello"))

# endswith() used to check if the string ends with a given value if yes then return true else false
message = "thank you"
print(message.endswith("you"))

# find() used to search for first occurance of the given value and returns the index value of it if not present then it returns -1 
message = "this is very good project"
print(message.find("is"))

# isalnum() returns true only if the entire string consists of A-Z, a-z, 0-9. If any other chracters or punctuations are present then it retuen flase 
msg = "mynameispratham"
print(msg.isalnum())

# isaplha() return true only if the entire string consists of A-Z, a-z. If any other chracters or punctuations , 0-9 are present then it retuen flase 
msg = "Pratham39"
print(msg.isalpha())

# islower() retruns true if all the characters are in string in lower case else false
msg = "pratham"
print(msg.islower())

# isprintable() returns true if all the values within the given are printable else false
msg = "hello how can i help you"
print(msg.isprintable())

msg2 = "hello how can i help you\n"
print(msg2.isprintable())

# isspace() return true if string contain white spaces else false 
msg = "   "
print(msg.isspace())

# istitle() returns true if the first letter of all the word in string is capital else false 
msg = "My Name Is Pratham"
print(msg.istitle())

# isupper() , startswith()

# swapcase() changes the character casing of the string , upper case are converted to lower case and lower case converted to upper case 

print(msg.swapcase())

# title() capitalizes each letter of the word within the string 
msg = "who are you"
print(msg.title())
