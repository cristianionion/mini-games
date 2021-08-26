import random

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

words = ['cat','dog','pineapple','banana', 'forest', 'panda', 'Minnesota', 'basketball', 'train', 'finger', 'fire',
        'river', 'lake', 'rapper', 'airplane', 'racecar', 'house', 'jeans', 'Monopoly', 'strawberry', 'kitten', 'softball', 'soccer', 'volleyball',
        'avatar', 'movie', 'shoes', 'paper', 'money', 'heist', 'park', 'waterfall']

def hangman(): # will not be case sensitive
    word = random.choice(words)
    word = word.lower() # makes all words lowercase
    word = list(word)
    hidden = "_" * len(word) # hides letters in random word from list
    hidden = list(word)
    max = 5 # max amount of wrong guesses before gg
    errors = 0 # number of errors so far

   # print(f"hidden word is: {hidden}")
    for i in range(len(hidden)):
        hidden[i] = "_"


    used = []

    print(hidden ,"\n")
    while errors != max:
        print("enter a single letter from a-z\n")
        guess = input()
        if guess not in used:
            used.append(guess)
            print("letters already used" ,used, "\n")

        if guess not in word:
            errors += 1


        for i in range(len(word)):
            if guess == word[i]:
                hidden[i] = guess
        print(hidden,"  errors left: ", max-errors, "\n")


        if hidden == word:
            a = ""   
            word = a.join(word)    
            return f'Success! Got the word {word} in {errors} errors'


    a = ""   
    word = a.join(word)    
    if errors >= max:
        return f'Sorry! Did not guess the word {word} in {max} errors'
    


# https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
# source for changing string to list so it can be muttable 

# https://www.geeksforgeeks.org/python-string-join-method/
# source for putting list back into string format