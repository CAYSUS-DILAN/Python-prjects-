import tkinter as tk
from tkinter import messagebox
import random


class WordGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Guessing Game")

        self.words = ["apple", "banana", "cherry", "orange", "grape", "kiwi", "melon", "peach"]
        self.secret_word = random.choice(self.words)
        self.attempts_left = 5

        self.label = tk.Label(root, text=f"Guess the word ({len(self.secret_word)} letters):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=20)
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.message_label = tk.Label(root, text=f"Attempts left: {self.attempts_left}")
        self.message_label.pack(pady=10)

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game, state=tk.DISABLED)
        self.restart_button.pack(pady=5)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=5)

    def check_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if guess == self.secret_word:
            messagebox.showinfo("Congratulations!", f"You guessed the word '{self.secret_word}' correctly!")
            self.restart_button.config(state=tk.NORMAL)
            self.guess_button.config(state=tk.DISABLED)
            self.entry.config(state=tk.DISABLED)
        else:
            self.attempts_left -= 1
            self.message_label.config(text=f"Attempts left: {self.attempts_left}")
            if self.attempts_left == 0:
                messagebox.showerror("Game Over", f"Out of attempts! The correct word was '{self.secret_word}'.")
                self.restart_button.config(state=tk.NORMAL)
                self.guess_button.config(state=tk.DISABLED)
                self.entry.config(state=tk.DISABLED)

    def restart_game(self):
        self.secret_word = random.choice(self.words)
        self.attempts_left = 5
        self.message_label.config(text=f"Attempts left: {self.attempts_left}")
        self.entry.config(state=tk.NORMAL)
        self.guess_button.config(state=tk.NORMAL)
        self.restart_button.config(state=tk.DISABLED)
        self.message_label.config(text=f"Guess the word ({len(self.secret_word)} letters):")


def main():
    root = tk.Tk()
    game = WordGuessingGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
