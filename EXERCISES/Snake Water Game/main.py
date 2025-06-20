# 1.Snake -->  2. Water
# 2. Water --> 3. Gun
# 3. Gun   --> 1. Snake

import random

choices = { 1 : "snake" , 2 : "water" , 3 : "gun"}

print("\n Snake Water Gun Game!! ")

user_points = 0
computer_points = 0

while True:
    try:
        user = int(input("\nEnter Your choice (1. Snake 2. Water 3. Gun ): "))
        if user not in [1 , 2 ,3]:
           print("Invalid choice!!, Please Enter 1. Snake , 2. Water , 3. Gun")
           continue
    except ValueError:
           print("Please Enter Number between 1 - 3")
           continue
    
    computer = random.randint(1 , 3)

    print(f"You Choose \"{choices[user]}\"")
    print(f"Computer choose \"{choices[computer]}\"")

    if ( computer == 1 and  user == 2 ) or (computer == 2 and user == 3 ) or (computer == 3 and user == 1 ):
            print("Computer Wins this round!!!")
            computer_points += 100
            if(computer_points == 500):
             print(f"Computer won the Game with the points {computer_points}")
             break
    elif( user == 1 and computer == 2 or user == 2 and computer == 3 or user == 3 and computer == 1 ):
            print("You Win this round!!!")
            user_points += 100
            if(user_points == 500):
             print(f"You won the Game with the points {user_points}")
             break
    else :
            print("Match Draw")
    print(f"🔢 Score => You: {user_points} | Computer: {computer_points}")