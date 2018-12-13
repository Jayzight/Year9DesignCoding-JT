import tkinter as tk
import random

root = tk.Tk()
root.title("Demo")


def reset():
	global l
	l = []
	canvas.create_rectangle(1,1,800,200, fill = 'grey70')

def keypressed(event):
	key = event.keysym.upper()
	l.append(key)

	canvas.create_rectangle(1,1,800,200, fill = 'grey70')
	canvas.create_text(400, 100, text=l)
	print (l)

def showButton():
	btn = tk.Button(root, text='CHANGE WORD', command=reset)
	btn.pack()

l = []
canvas = tk.Canvas(root, width = 800, height = 200, bg= 'grey70')
canvas.pack()

showButton()


root.bind("<Key>",keypressed)

root.mainloop()