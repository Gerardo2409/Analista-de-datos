import random


def choose_word():
    words = ["python", "programming", "computer", "hangman", "developer", "openai", "language"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed = ''
    for letter in word:
        if letter in guessed_letters:
            displayed += letter
        else:
            displayed += '_'
    return displayed

def hangman():
    max_attempts = 6
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 0

    print("Bienvebido al ahorcado!")
    print(display_word(word_to_guess, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Correct!")
        else:
            attempts += 1
            print("Incorrect!")
            print(f"Attempts left: {max_attempts - attempts}")

        print(display_word(word_to_guess, guessed_letters))

        if set(word_to_guess) <= set(guessed_letters):
            print("Congratulations! You've guessed the word!")
            break

        if attempts >= max_attempts:
            print("You've run out of attempts. The word was:", word_to_guess)
            break

if __name__ == "__main__":
    hangman()
