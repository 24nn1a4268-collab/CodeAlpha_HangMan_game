import random

# Step 1: Create a list of predefined words
words = ["apple", "tiger", "house", "python", "flower"]

# Step 2: Randomly select one word
secret_word = random.choice(words)

# Step 3: Create an empty list to display guessed letters
guessed_word = []

# Step 4: Fill the guessed_word list with underscores
for letter in secret_word:
    guessed_word.append("_")

# Step 5: Set the maximum incorrect guesses
wrong_guesses = 0
max_wrong_guesses = 6

# Step 6: Store guessed letters
guessed_letters = []

print("====== HANGMAN GAME ======")
print("Guess the hidden word!")

# Step 7: Continue until the game ends
while wrong_guesses < max_wrong_guesses and "_" in guessed_word:

    # Display current word
    print("\nCurrent Word:", " ".join(guessed_word))
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    # Take input
    guess = input("Enter a letter: ").lower()

    # Check if only one letter is entered
    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add guessed letter
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in secret_word:
        print("Correct Guess!")

        # Reveal matching letters
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess

    else:
        print("Wrong Guess!")
        wrong_guesses += 1

# Step 8: Display result
if "_" not in guessed_word:
    print("\nCongratulations!")
    print("You guessed the word:", secret_word)
else:
    print("\nGame Over!")
    print("The correct word was:", secret_word)