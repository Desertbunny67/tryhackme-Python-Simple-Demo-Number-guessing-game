import random

secret = random.randint(1,20)
tries = 0
guess = 0

print("do you want to play a game of guessing a number between 1-20")
answer = input("yes/no:")
if answer=="yes":
    print("im thinking a number between 1-20")
    while guess != secret:

        
        guess = int(input("take a guess:"))
        tries += 1
        if guess == secret:
    
            print(f"you got it in {tries} tries")

    
        elif guess > secret:
    
            print("too high try again")
    
        elif guess < secret:
    
            print("too low try again")
else:
     print("maybe next time!")
    


