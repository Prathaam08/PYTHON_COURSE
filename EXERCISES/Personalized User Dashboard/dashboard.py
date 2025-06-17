# ✅ Features
# Ask for name, age, and birth year	
# Calculate and show user age	
# Reverse their name
# Show name in uppercase and lowercase
# Swap favorite numbers

print("-----------------||USER DASHBOARD||------------------------------")
name = str(input("Enter you name:"))
birth_year = int(input("Enter your Birth Year:"))
current_year = 2025

age = current_year - birth_year

print(name.capitalize(), "sir you age is:",age)

print("Reverse of your name is :",name[::-1])

print(name.upper())
print(name.lower())

print("------------||Swapping your fav number||---------------------")

num1 = input("Enter the first number:")
num2 = input("Enter the second number:")

num1 , num2 = num2 , num1

print("Swapping of your fav number is:" , num1,num2)