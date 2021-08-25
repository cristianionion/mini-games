import random
# game will randomly select an integer between 0-100
# user guesses number and is given hints based on guess

def guessr():

    target = random.randint(0,100) #set the number that needs to be guessed
    max = 101 # maximum amount of guesses before answer is revealed

    print("guess a number from 0-100!")

    for i in range(max):
        guess = int(input()) # takes guess from user and converts str -> int
        if target == guess:
            success = f"you guessed the number {target} in {i+1} tries"
            return success
        elif target > guess:
            print("guess was too low")
        elif target < guess:
            print("guess was too high")
    
    fail = f"ran out of attempts... correct number was: {target}"
    return fail