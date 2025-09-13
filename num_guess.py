import tkinter as tk
import random

secret = random.randint(1, 100)
attempts = 0

def check():
    global secret,attempts
    attempts += 1
    guess = int(entry.get())
    if guess < secret:
        label.config(text="Too low!")
    elif guess > secret:
        label.config(text="Too high!")
    else:
        label.config(text=f"Yes {secret}, you guessed it in {attempts} attempts! Starting new game...")
        secret = random.randint(1, 100)
        attempts = 0
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Guess the Number")

entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="Check", command=check)
check_button.pack()

label = tk.Label(root, text="Guess a number between 1 and 100")
label.pack()

root.mainloop()
