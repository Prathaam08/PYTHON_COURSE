question = ["What is your name?" , "India's capital."]
answer = ["Pratham" , "Delhi"]
priceWon = 0

for i in range(len(question)):
    print()
    print(question[i])
    userAns = (input("Enter your answer OR if you want to quit press 0 :").title())
    if(userAns == "0"):
        print("You quit the contest")
        print("Your take home money is",priceWon)
        break 

    if( userAns == answer[i]):
       print("correct answer")
       priceWon = priceWon + 10000 
       print("You won ₹" ,priceWon)
    else:
        print("incorrect answer")  
        priceWon
        break