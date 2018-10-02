import tkinter as tk

def enter():
	output.insert(tk.INSERT,guess)


final = "---------------------------------"



window = tk.Tk()
window.title("Hangman")

text1 = tk.Label(window, text="Welcome to Hangman!")
text1.pack(pady = 10)

text2 = tk.Label(window, text="You have 8 attempts to guess the word.")
text2.pack(pady = 10)

output = tk.Text(window, width=10, height=2, borderwidth=3, relief=tk.GROOVE)
output.pack()

label1 = tk.Label(window, text="Guess a Letter:")
label1.pack(pady = 10)

guess = tk.Entry(window)
guess.pack(pady = 10, padx = 20)

btn = tk.Button(window, text="Submit", command=enter)
btn.pack(pady = 10, padx = 10)


label2 = tk.Label(window, text="Guessed Letters")
label2.pack(pady = 10)

guessed = tk.Text(window, width=50, height=4, borderwidth=3, relief=tk.GROOVE)
guessed.pack(pady = 10, padx = 20)

window.mainloop()

