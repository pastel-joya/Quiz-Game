import random

welcome = "Welcome to rock, paper, scissor game"
print(welcome.center(40, "."))

a = "rock"
b = "paper"
c = "scissor"

print("a = rock \nb = paper \nc = scissor")

choices = [a, b, c]

random_choose = random.choice(choices)


play = input("choose one between (a, b, c): ").strip().lower()


if play == "a" and random_choose == b:
    print("you lose")
elif play == "a" and random_choose == c:
    print("you won")
elif play == "b" and random_choose == c:
    print("you lose")
elif play == "b" and random_choose == a:
    print("you won")
elif play == "c" and random_choose == a:
    print("you lose")
elif play == "c" and random_choose == b:
    print("you won")
elif play == "a" and random_choose == a:
    print("draw")
elif play == "b" and random_choose == b:
    print("draw")
elif play == "c" and random_choose == c:
    print("draw")
else:
    print("invalid choice! please type a, b, c.")


print("computer choose", random_choose)