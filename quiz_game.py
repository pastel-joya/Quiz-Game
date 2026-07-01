welcome = "Welcome to the Quize Game"
print(welcome.center(65, "*"))

score = 0

play = input("Do you want to play the game? ")
if play != "yes":
    print("okay!")
    quit()
else:
    print("let's play, choose a answer between a , b or c".center(65, "*"))

question_1 = input("I have no life but I can die. what Am I? \n a. Robot, \n b. Star, \n c. Battery \n ")

if question_1.lower() == "c" :
    print("correct!")
    score += 1
else:
    print("worng, the correct answer is c")



question_2 = input("Which animal eats itself when hungry? \n a. Snake, \n b. Scorpion, \n c. Crab \n " )

if question_2.lower() == "b" :
    print("correct!")
    score += 1
else:
    print("worng, the correct answer is b")




question_3 = input("Which animal cannot look up at the sky? \n a. Snake, \n b. Elephant, \n c. Pig \n " )

if question_3.lower == "c" :
    print("correct!")
    score += 1
else:
    print("worng, the correct answer is c")




question_4 = input("What is the normal body temperature? \n a. 35 ℃, \n b. 37℃, \n c. 39℃ \n " )

if question_4.lower() == "b" :
    print("correct!")
    score += 1
else:
    print("worng, the correct answer is b")




question_5 = input("Whice fruit is unsafe during pregnancy? \n a. Apple, \n b. Banana, \n c. Papaya \n " )

if question_5.lower() == "c" :
    print("correct!")
    score += 1
else:
    print("worng, the correct answer is c")




print("your total score is", score, ",u got 3 answers right")