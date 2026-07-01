import random
while True:
    take_num = input("Take a number: ")

    if take_num.isdigit():
        take_num = int(take_num)

        if take_num > 0:
            break

        else:
            print("Enter a number larger than 0")

    else:
        print("Enter a digit next time")

random_num = random.randrange(0, take_num)

guess = 0 

while True:
    guess += 1
    guess_num = input("guess the number: ")
    
    if guess_num.isdigit():
        guess_num = int(guess_num)

    else:
        print("Enter a digit next time")
        continue

        
    if guess_num == random_num:
        print("Yahooo!, you got it right.")
        break
    elif guess_num < random_num:
        print("you were bellow the number")
    else:
        print("you were above the number")

print("You got it in", guess, "guesses")   
    


        