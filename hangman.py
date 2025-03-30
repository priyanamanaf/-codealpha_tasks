import random

def choose_word():
    return random.choice(["history", "maths", "physics", "chemistry", "english"])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        
        display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
        print("\nWord:", display)
        print(f"Attempts left: {attempts}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1
            print("Wrong guess!")

        if set(word) <= guessed_letters:
            print("\nCongratulations! You guessed the word: {word}")
            return

    print("\nGame over! The word was: {word}")

if __name__ == "__main__":
    hangman()
