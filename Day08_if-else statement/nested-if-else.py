num = int(input("Enter the number:"))
if (num < 0 ):
    print("number is negative")
elif (num > 0 ):
    if(num < 20):
        print("number is between 1-20")
    elif(num >= 20 and num <= 40):
        print("number is between 20-40")
    elif(num >= 40 and num <= 60):
        print("number is between 40-60")
    else:
        print("number is greater than 60")
else:
    print("number is zero")