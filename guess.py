import random 
N = random.randint(1, 100)
print(N)
guess = 0
while guess !=N:
    guess = int(input("enter the number"))

    if guess < N:
        print("two low")
    elif guess >N :
        print("to high")
    else:
        print("you guess the number")