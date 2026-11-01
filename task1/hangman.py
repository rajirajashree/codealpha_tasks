import random
# Five predefined words
words = ["python", "computer", "student", "coding", "program"]
secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6
print("=== Hangman Game ===")
print("Guess the hidden word one letter at a time.")
print(f"You can make up to {max_wrong_guesses} incorrect guesses.")
while wrong_guesses < max_wrong_guesses:
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word.strip())
    print("Incorrect guesses left:", max_wrong_guesses - wrong_guesses)
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You guessed the word:", secret_word)
        break
    guess = input("Enter one letter: ").lower().strip()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter exactly one alphabet letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter. Try another.")
        continue
    guessed_letters.append(guess)
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Incorrect guess!")
if wrong_guesses == max_wrong_guesses and not all(
    letter in guessed_letters for letter in secret_word
):
    print("\nGame over! The word was:", secret_word)