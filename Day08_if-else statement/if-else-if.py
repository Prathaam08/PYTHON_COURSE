age = int(input("Enter your age:"))

if(age < 18):
    print("You are Teenager")
elif(age >= 60):
    print("You are senior citizen")
elif(age >= 18):
    print("You are adult")
else:
    print("invalid input")
print("Goodbye")
