sum = 0
while True:
    userInput = input("Enter the item price or type \"q\" to exit: ")
    if userInput!= "q":
        sum = sum + int(userInput)
        print(f"Your Total so far is {sum}\n")
    else:
        print("Thank for purchase!!")
        print(f"The Total Price is ₹{sum}")
        break