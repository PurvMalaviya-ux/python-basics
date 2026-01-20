import random as ran

print("Hello There Welcome To My Code")
print("                              ")
print("Let's Build Something Amazing Togethor")
print("This is a Number Guessing Game")

ran = ran.randint(1,100)
guess = None


while guess != ran:
    guess = int(input("Guess a number between 1 and 100 :"))
    if guess < ran:
        print("Too Low! Try Again")
    elif guess > ran:
        print("Too High! Try Again")   
    else:
        print("Congratulations! You guessed It Right! ") 