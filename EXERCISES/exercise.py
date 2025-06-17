#Write a Python script that takes two numbers as input and performs basic arithmetic operations
# a = int(input("Enter the number 1:"))
# b = int(input("Enter the number 2:"))

# print("The value of", a ,"+" , b , "is:", a+b)
# print("The value of", a ,"-" , b , "is:", a-b)
# print("The value of", a ,"*" , b , "is:", a*b)
# print("The value of", a ,"/" , b , "is:", a/b)


#Write a program that takes the user's name as input and greets them with a personalized message.
# name = str(input("Enter your name:"))
# print("Welcome " + name + " sir")

#Write a program that takes your birth year and prints your current age.

# a = int(input("Enter your \"Birth Year\":"))
# print("Your current \"AGE\" is", 2025-a)

#Take two numbers from the user and swap them.

# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))

# print("Before Swapping")
# print("num1 is ", num1)
# print("num2 is ", num2)

# temp = num1
# num1 = num2 
# num2 = temp

# print("After Swapping")
# print("num1 is :" , num1)
# print("num2 is :" , num2)

#Create a simple BMI calculator:
#Input: weight (kg), height (m)
#Output: BMI = weight / (height ** 2)

# weight = float(input("Enter your weight:"))
# height = float(input("Enter your height:"))

# print("Your \"BMI\" is: " , weight/(height**2) )

#Swap two numbers without using a temporary variable.
# a= 20
# b= 40
# a, b = b , a
# print(a,b)

# #Create a program that asks for the user's name and age, then prints a greeting.
# name = str(input("Enter your \"name\":"))
# age = int(input("Enter your \"age\":"))
# print("Your name is" , name , "and your age is",age)   

# #Extract the first and last characters of a string entered by the user.
# print(name[0], name[6])

# #Reverse a string using slicing.
# print(name[::-1])


# import time
# # timestap = int(time.strftime('%H'))
# timestap = 17
# print(timestap)
# if(timestap < 12 ):
#     print("Sir good morning")
# elif(timestap >= 18):
#     print("sir good evening")
# elif(timestap >= 12):
#     print("sir good afternoon")

# Print numbers from 1 to 50, but skip multiples of 5 using the continue statement.
# for i in range(50):
#  if ( i % 5 == 0):
#     continue
#  print(i)

