from words import words
from random import choice
from hangman_drawings import lives_visual_dictionary
from string import ascii_uppercase


def select_word(words):
    word = choice(words)
    return word.upper()


def hangman():
    print("---------------------------------------------")
    print("------- Welcome To The Hanghman Game! -------")
    print("---------------------------------------------")

    word = select_word(words)
    letters_to_guess = set(word)
    alphabet = set(ascii_uppercase)
    guessed_letters = set()

    lives = len(lives_visual_dictionary) - 1  # 7 in this case

    while len(letters_to_guess) > 0 and lives > 0:
        print(
            f"\nYou have {lives} left and have written the letters: {' '.join(guessed_letters)}"
        )

        word_list = [letter if letter in guessed_letters else "-" for letter in word]
        print(lives_visual_dictionary[lives])
        print(f"Word: {' '.join(word_list)}")

        user_letter = input("Write a letter: ").upper()

        if user_letter in alphabet - guessed_letters:
            guessed_letters.add(user_letter)

            if user_letter in letters_to_guess:
                letters_to_guess.remove(user_letter)
            else:
                lives -= 1
                print(f"\nYour letter, {user_letter} is not in the word!")

        elif user_letter in guessed_letters:
            print(f"\nYou already wrote the letter {user_letter}")
        else:
            print(f"\nThe letter {user_letter} is not valid!")

    if lives == 0:
        print(lives_visual_dictionary[lives])
        print(f"\nHanged! You've lost! The word was {word}")
    else:
        print(f"\nCongratulations! You guessed the word {word}!")


hangman()
