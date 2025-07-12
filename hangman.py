import random

def hangman():
    words = ["samsung", "apple", "aeroplane", "bicycle", "smartphone"]
    word_to_guess = random.choice(words)
    guessed_word = ["_"] * len(word_to_guess)  
    attempts = 6  
    guessed_letters = []  

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print(f"You have {attempts} incorrect guesses allowed.")
    print(" ".join(guessed_word)) 

    while attempts > 0 and "_" in guessed_word:
        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha(): 
            print("Please enter a valid single letter.")
            continue
        if guess in guessed_letters:  
            print("You already guessed that letter. Try again.")
            continue
        guessed_letters.append(guess)  
        if guess in word_to_guess:  
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess  
        else:  
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word. You have {attempts} attempts left.")

        print(" ".join(guessed_word))  

    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word_to_guess)
    else:
        print("\nGame over! The word was:", word_to_guess)
hangman()
