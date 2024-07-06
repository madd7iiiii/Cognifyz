import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.lower_limit = 1
        self.upper_limit = 100
        self.secret_number = random.randint(self.lower_limit, self.upper_limit)

        self.attempts = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Guess the number between {} and {}: ".format(self.lower_limit, self.upper_limit))
        self.label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.submit_button = tk.Button(self.master, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess == self.secret_number:
                messagebox.showinfo("Congratulations", "You guessed the correct number {} in {} attempts.".format(self.secret_number, self.attempts))
                self.master.destroy()
            elif guess < self.secret_number:
                messagebox.showinfo("Incorrect Guess", "Too low! Try again.")
            else:
                messagebox.showinfo("Incorrect Guess", "Too high! Try again.")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

def main():
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()










