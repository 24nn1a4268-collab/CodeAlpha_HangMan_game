# 🎮 Hangman Game in Python

## 📌 Project Overview

This project is a simple **text-based Hangman Game** developed in **Python**. The game randomly selects a word from a predefined list, and the player attempts to guess the word one letter at a time. The player has a maximum of **6 incorrect guesses** to reveal the complete word before the game ends.

This project is designed to strengthen fundamental Python programming concepts, including loops, conditional statements, lists, strings, functions, and the `random` module.

---

## 🚀 Features

* Randomly selects a word from a predefined list.
* Displays the hidden word using underscores.
* Accepts one-letter guesses from the user.
* Reveals correctly guessed letters in their correct positions.
* Limits the player to **6 incorrect guesses**.
* Prevents duplicate guesses.
* Displays a winning or losing message at the end of the game.

---

## 🛠️ Technologies Used

* Python 3
* Random Module

---

## 📚 Concepts Covered

* Variables
* Lists
* Strings
* Loops (`while` and `for`)
* Conditional Statements (`if`, `elif`, `else`)
* User Input
* Random Module
* Basic Game Logic
* Input Validation

---

## 📂 Project Structure

```text
Hangman-Game/
│── hangman.py
│── README.md
```

---

## ▶️ How to Run

1. Clone this repository.

```bash
git clone https://github.com/your-username/Hangman-Game.git
```

2. Navigate to the project folder.

```bash
cd Hangman-Game
```

3. Run the program.

```bash
python hangman.py
```

---

## 💻 Sample Output

```text
====== HANGMAN GAME ======

Current Word: _ _ _ _ _

Wrong guesses left: 6

Enter a letter: a

Correct Guess!

Current Word: a _ _ _ _

Enter a letter: p

Correct Guess!

Current Word: a p p _ _

...

Congratulations!
You guessed the word: apple
```

---

## 🎯 Learning Outcomes

By completing this project, I learned how to:

* Build a simple console-based game using Python.
* Apply loops and conditional statements to control program flow.
* Work with lists and strings to update and display game progress.
* Use the `random` module for random word selection.
* Validate user input and handle repeated guesses.
* Implement basic game logic using problem-solving skills.

---

## 🔮 Future Enhancements

* Add multiple difficulty levels.
* Read words from an external file.
* Display ASCII Hangman graphics.
* Add score tracking.
* Allow multiple rounds of play.
* Build a graphical user interface (GUI) using Tkinter or Pygame.

---

## 👩‍💻 Author

**Jaya Sri Chenna**

Python Developer | Learning Data Structures & Algorithms | Exploring Artificial Intelligence and Machine Learning

If you found this project helpful, feel free to ⭐ the repository!
