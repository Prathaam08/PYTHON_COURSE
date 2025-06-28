def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num -1)

userInput = int(input("Enter the numbert: "))
print(f"The factorial of number {userInput} is {factorial(userInput)}")