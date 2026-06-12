import random
num = random.randint(1,50)
guess = 0
while guess != num:
    guess = int (input("Enter the number"))
    if (guess < num):
        print("guess higher")
    elif(guess > num):
        print("guess lesser")
    else:
        print("your guess is correct")

