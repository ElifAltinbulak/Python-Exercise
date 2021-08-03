#finalproject
print("****Welcome Knowledge Competition****")
questıons=["1-Which is the first animal to be domesticated?",
           "2-Which one is used for direction function?",
           "3-Which of the fish species is the mammal?",
           "4-Which is the planet with the largest satellite?",
           "5-Which animal is more resistant to the desert?",
           "6-In which environment does sound propagate fastest?",
           "7-Which is a natural light source?",
           "8-Which animal is a reptile?",
           "9-Which one is an organelle?",
           "10-What is the derivative of 1?"]
answers=["A)Dog B)Fish C)Elephant D)Horse E)Empty",
         "A)Tree B)Flower C)North Star D)Rock E)Empty ",
         "A)Anchovy B)Whale C)Shark D)Perch E)Empty ",
         "A)World B)Anthem C)Saturn D)Jupiter E)Empty",
         "A)Dog B)Horse C)Camel D)Chameleon E)Empty ",
         "A)Solid B)Liquid C)Gas D)Board E)Empty ",
         "A)Lamp B)Oil Lamp C)Firefly D)Moon E)Empty ",
         "A)Turtle B)Mole C)Hedgehog D)Squirrel E)Empty",
         "A)DNA B)RNA C)MRNA D)Lisosome E)Empty ",
         "A)2 B)-1 C)0 D)1 E)Empty "]
correct=["A","C","B","D","C","A","C","A","D","C"]
s,a=0,0
def start():
    score=0
    for i in range(10):
        global s,a
        print(f"{questıons[i]}")
        print(answers[a])
        ya=input("Please write the correct answer: ")
        if (ya.upper()==correct[s]):
            print("Your answer is CORRECT")
            score+=10
        elif (ya.upper()=="E"):
            print("Your answer is EMPTY")
            score-=0
        else:
            print("Your answer is WRONG")
            score-=0
        i+=1
        s+=1
        a+=1
    print(f"Your Score: {score}")
    if score>=50:
        print("Successful")
    else:
        print("Unsuccessful")
start()
