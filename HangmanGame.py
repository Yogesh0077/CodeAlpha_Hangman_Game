import tkinter as tk
import random

# List of words to choose from
words = ["python", "programming", "hangman", "computer", "developer", "game", "algorithm"]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("500x300")
        
        self.start_new_game()

        # GUI components
        self.word_label = tk.Label(root, text=self.display_word, font=('Arial', 24))
        self.word_label.pack(pady=20)

        self.input_label = tk.Label(root, text="Enter a letter:", font=('Arial', 14))
        self.input_label.pack()

        self.entry = tk.Entry(root, font=('Arial', 14))
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(root, text="Guess", font=('Arial', 14), command=self.make_guess)
        self.guess_button.pack(pady=10)

        self.incorrect_label = tk.Label(root, text="Incorrect guesses left: 6", font=('Arial', 14))
        self.incorrect_label.pack(pady=20)

        self.result_label = tk.Label(root, text="", font=('Arial', 14), fg="red")
        self.result_label.pack(pady=20)

        self.restart_button = tk.Button(root, text="Restart", font=('Arial', 14), command=self.restart_game)
        self.restart_button.pack(pady=10)

    def start_new_game(self):
        """Start a new game by initializing the word, guessed letters, and incorrect guesses."""
        self.word = self.choose_word()
        self.guessed_letters = []
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 6
        self.display_word = self.create_display_word()
        
    def choose_word(self):
        """Choose a random word from the list."""
        return random.choice(words)

    def create_display_word(self):
        """Create a string to represent the word with blanks for unguessed letters."""
        return ''.join(['_' if letter not in self.guessed_letters else letter for letter in self.word])

    def make_guess(self):
        """Make a guess by the player."""
        guess = self.entry.get().lower()

        if len(guess) != 1 or not guess.isalpha():
            self.result_label.config(text="Please enter a valid letter.")
            return

        if guess in self.guessed_letters:
            self.result_label.config(text="You already guessed that letter.")
            return

        self.guessed_letters.append(guess)

        if guess in self.word:
            self.result_label.config(text=f"Good guess! {guess} is in the word.")
        else:
            self.incorrect_guesses += 1
            self.result_label.config(text=f"Wrong guess! {self.max_incorrect_guesses - self.incorrect_guesses} incorrect guesses left.")

        self.update_game_state()

    def update_game_state(self):
        """Update the game state (word display, incorrect guesses, and check win/loss)."""
        self.display_word = self.create_display_word()
        self.word_label.config(text=self.display_word)

        self.incorrect_label.config(text=f"Incorrect guesses left: {self.max_incorrect_guesses - self.incorrect_guesses}")

        if self.incorrect_guesses >= self.max_incorrect_guesses:
            self.result_label.config(text=f"Game over! The word was: {self.word}")
            self.entry.config(state='disabled')
            self.guess_button.config(state='disabled')

        elif '_' not in self.display_word:
            self.result_label.config(text="Congratulations! You've guessed the word!")
            self.entry.config(state='disabled')
            self.guess_button.config(state='disabled')

    def restart_game(self):
        """Restart the game by resetting the state and starting a new game."""
        self.start_new_game()
        self.entry.config(state='normal')
        self.guess_button.config(state='normal')
        self.result_label.config(text="")
        self.incorrect_label.config(text=f"Incorrect guesses left: {self.max_incorrect_guesses}")
        self.word_label.config(text=self.display_word)

def main():
    root = tk.Tk()
    app = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
