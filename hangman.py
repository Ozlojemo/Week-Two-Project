
import random
import sys

words =["lengths","lucky", "luxury", "lymph", "subway", "swivel"]

#Add a functioon that randomly selects one word from the list
def select_word(words):
    return random.choice(words)

#Variables for the game
#Remaining_attempts
#guessed_letters

remaining_attempts= 6
guessed_letters =" "
#define the loop- to show whether the words have been guesed correctly
def print_secret_word(secret_word, guessed_letters):
    for letter in secret_word:
        if letter in guessed_letters:
            print (" ", letter, end="")
        else:
            print(" _ ", end="")
    print("\n")
    
print("Welcome to the Hangman Game! Let's see if you can guess this word!\n")
secret_word = select_word(words)

#Add the function
def is_guess_in_secret_word(guess, secret_word):
    if len(guess) > 1 or not guess.isalpha():
        print("Only single letters are allowed. Unable to continue...")
        sys.exit()
    else:
        if guess in secret_word:
            return True
        else:
            return False

def get_unique_letters(word):
    return "".join(set(word))

while remaining_attempts > 0 and len(guessed_letters) < len(get_unique_letters(secret_word)):
    guess = input("Guess a letter: ")
    guess_in_secret_word = is_guess_in_secret_word(guess, secret_word)

    if guess_in_secret_word:
        if guess in guessed_letters:
            print("You have already guessed the letter {}".format(guess))
        else:
            print("Yes! The letter {} is part of the secret word".format(guess))
            guessed_letters= guessed_letters + guess

    else:
        print("No! The letter {} is not part of the secret word".format(guess))
        remaining_attempts =remaining_attempts- 1 
if len(guessed_letters) == len(get_unique_letters(secret_word)):
    print("Well done, you have won this game!\n")
else:
    print("Sorry, you have lost this game!\n")     
    print(secret_word)
