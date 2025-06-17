questions = [
    ["What is your name?" , "Kalpesh" , "Pratham" , "Nitin" , "Rupesh" , 2],
    ["What is the capital of India?" , "Mumbai" , "Chennai" , "Delhi" , "Kolkata" , 3],
    ["Which planet is known as the Red Planet?" , "Earth" , "Mars" , "Venus" , "Jupiter" , 2],
    ["Who wrote the Ramayana?" , "Valmiki" , "Tulsidas" , "Kalidas" , "Ved Vyas" , 1],
    ["What is the boiling point of water?" , "90°C" , "50°C" , "100°C" , "120°C" , 3],
    ["Which gas do plants absorb from the atmosphere?" , "Oxygen" , "Hydrogen" , "Nitrogen" , "Carbon Dioxide" , 4],
    ["Who is the current Prime Minister of India?" , "Rahul Gandhi" , "Narendra Modi" , "Amit Shah" , "Arvind Kejriwal" , 2],
    ["Which animal is known as the Ship of the Desert?" , "Elephant" , "Horse" , "Camel" , "Donkey" , 3],
    ["Which is the largest ocean in the world?" , "Indian Ocean" , "Pacific Ocean" , "Atlantic Ocean" , "Arctic Ocean" , 2],
    ["Which is the national bird of India?" , "Sparrow" , "Peacock" , "Parrot" , "Eagle" , 2],
    ["What is H2O commonly known as?" , "Salt" , "Oxygen" , "Water" , "Hydrogen" , 3],
    ["Which instrument is used to measure temperature?" , "Thermometer" , "Barometer" , "Speedometer" , "Altimeter" , 1],
    ["Which festival is known as the Festival of Lights?" , "Holi" , "Diwali" , "Eid" , "Christmas" , 2],
    ["What is the square root of 64?" , "6" , "7" , "8" , "9" , 3],
    ["Who invented the light bulb?" , "Isaac Newton" , "Albert Einstein" , "Thomas Edison" , "Nikola Tesla" , 3],
    ["What is the largest continent on Earth?" , "Africa" , "Asia" , "Europe" , "Australia" , 2],
    ["How many colors are there in a rainbow?" , "5" , "6" , "7" , "8" , 3]
]


levels = [1000 , 2000 , 3000 , 5000 , 10000 , 20000 , 40000 , 80000 , 160000 , 320000 , 640000 , 1250000 , 2500000 , 5000000 , 7500000 , 10000000 , 75000000]

money = 0

for i in range(0 , len(questions)):
    question = questions[i]
    print(f"\n{i+1}. Question for ₹ {levels[i]}")
    print(question[0])
    print(f"a. {question[1]}                b. {question[2]}")
    print(f"c. {question[3]}                d. {question[4]}")      
    reply = int(input("Enter your answer (1-4) or Press \"0\" to quit: "))
    if ( reply == 0 ):
        print("You quit the contest ")
        print(f"Congratulation You won ₹ {levels[i-1]}")
        break
    if (reply == question[5] ):
        print(f"Correct answer, You won ₹ {levels[i]}")
        if ( i == 4):
            money = 10000
        elif ( i == 9):
            money = 320000
        elif ( i == 14):
            money = 7500000
    else:
        print("Wrong answer!")
        print(f"Your take home money is ₹ {money}")
        break
        