import random

# Predefined list of words
words = ["python", "hangman", "coding", "intern", "project"]

# Randomly select a word
word = random.choice(words)
guessed_letters = []
attempts = 6

print("🎯 Welcome to Hangman Game!")
print("You have 6 incorrect guesses.\n")

while attempts > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word.strip())

    # Check if player has won
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word correctly.")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.\n")
    elif guess in word:
        guessed_letters.append(guess)
        print("✅ Good guess!\n")
    else:
        guessed_letters.append(guess)
        attempts -= 1
        print("❌ Wrong guess!")
        print("Remaining attempts:", attempts, "\n")

# If attempts are exhausted
if attempts == 0:
    print("💀 Game Over!")
    print("The correct word was:", word)
