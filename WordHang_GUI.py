import tkinter as tk
from PIL import Image
import random
from tkinter import messagebox as tkMessageBox

root = tk.Tk()
root.title("WordHang")
root.configure(background='grey21')
font = 15
fontdata = [15,1]

def on_enter(e):
    btnStat1['background'] = 'white'
def on_leave(e):
    btnStat1 ['background'] = 'red'

def vocab():
	root3 = tk.Tk()
	root3.title("Vocabulary")
	vocabtxt = tk.Text(root3, width = 40, height = 7, background = 'grey90')
	vocabtxt.pack(padx = 7 ,pady = 14)
	vocabtxt.insert(tk.INSERT, '\n'.join(wordlist))
	vocabtxt.config(state="disabled")

def settings():
	root2 = tk.Tk()
	root2.title("Settings")

	accesslabel = tk.Label(root2, text = "Accessibility Options")
	accesslabel.pack(pady = (20,2), padx = 50, ipady=9)

	accessbtn = tk.Button(root2, text = "Bigger Text")
	accessbtn.pack(padx = 50, ipadx= 25, ipady=7)

	accessbtn2 = tk.Button(root2, text = "Color Contrast")
	accessbtn2.pack(pady = 10, padx = 50, ipadx= 15, ipady=7)

	accessbtn3 = tk.Button(root2, text = "Text to Speech")
	accessbtn3.pack(padx = 50, ipadx= 15, ipady=7)

def generateNewWord():
	global canswer
	global answer
	global life
	global guessed
	global guessedOutput
	answer = []
	canswer = []
	rand = random.randint(0,len(wordlist)-1)
	wordanddef = wordlist[rand]
	locstar = wordanddef.index("*")
	solution[0] = (wordanddef[0:locstar])
	solution[1] = (wordanddef[locstar + 1:])
	for i in range (0, len(solution[0]),1):
		canswer.append(solution[0][i])
	for i in range (0, len(canswer),1):
		answer.append("__")
	guessed = []
	guessedOutput = " "
	drawCanvas()
	life = 10
	canvas.create_rectangle(514, 335, 740, 400, fill='grey90', outline='grey4')
	canvas.create_text(624, 355, anchor="nw", text= life)
	canvas.create_text(181, 200, anchor="nw", text= "Definition: ", font = font, disabledfill='grey1', activefill = 'red')
	canvas.create_text(30, 353, anchor = tk.SW,text = guessedOutput, font = ("Times",15), disabledfill='grey1', activefill = 'red')

def keypressed(event):
	global life
	key = event.keysym.upper()
	print (key)
	if key.isalpha() == True:
		found = False
		for i in range(0, len(canswer),1):
			if canswer[i] == key:
				print("CORRECT LETTER")
				answer[i] = key
				found = True
			canvas.create_text(200 + xshift[0]*i, 120, text = answer[i]+" ", anchor = 'center', font = ("Times",30), disabledfill='grey1', activefill = 'red')
		if found == False:
			if key not in guessed:
				life = life - 1
				canvas.create_rectangle(514, 335, 740, 400, fill='grey90', outline='grey4')
				canvas.create_text(624, 355, anchor="nw", text= life)
				guessed.append(key)
				guessedOutput = ""
				for i in range(0, len(guessed),1):
					if i != 0 and i % 15 == 0:
						guessedOutput = guessedOutput + "\n"
					guessedOutput = guessedOutput + guessed[i]+" "

				canvas.create_rectangle(22, 335, 248, 400, fill='grey90', outline='grey4')
				canvas.create_text(30, 353, anchor = tk.SW, text = guessedOutput, font = ("Times",15), disabledfill='grey1', activefill = 'red')
		if canswer == answer:
			tkMessageBox.showinfo("You Win", "You guessed the correct word. Click New Word to continue.")
		if life == 0:
			tkMessageBox.showinfo("You Lose", "You ran out of lives. The word was *" + str(solution[0]) + "* Click New Word to continue.")
	else:
		tkMessageBox.showerror("Error", "Please enter a valid letter.")

def drawCanvas():
#Guessed Letters
	guessedlettersbox = canvas.create_rectangle(22, 335, 248, 400, fill='grey90', outline='grey4')
	guessedletterslabel = canvas.create_rectangle(22, 295, 248, 325, fill='grey75', outline='grey4')
	guessedlettersword = canvas.create_text(137, 310, text= "Guessed Letters", anchor="center", font = font, fill='grey1', activefill = 'white')
#Time
	timebox = canvas.create_rectangle(267, 335, 493, 400, fill='grey90', outline='grey4')
	timelabel = canvas.create_rectangle(267, 295, 493, 325, fill='grey75', outline='grey4')
	timeword = canvas.create_text(380, 310, text= "Time Left", anchor="center", font = fontdata[0], fill='grey1', activefill = 'white')
#Lives left
	canvas.create_rectangle(514, 335, 740, 400, fill='grey90', outline='grey4')
	canvas.create_rectangle(514, 295, 740, 325, fill='grey75', outline='grey4')
	canvas.create_text(627, 310, text= "Lives Left", anchor="center", font = font, fill='grey1', activefill = 'white')
#Defintion
	canvas.create_rectangle(177, 196, 632, 248, fill='#fff', outline='grey4')
	canvas.create_text(181, 200, anchor="nw", text= "Definition: ", font = font, disabledfill='grey1', activefill = 'red')
	canvas.create_text(245, 200, text= solution[1], anchor="nw", font = (15), fill='red', activefill = 'grey1')
#Word Box
	canvas.create_rectangle(140, 85, 664, 162, fill='#fff', outline='grey4')

#************************************* FETCHING FILE *********************************
import random
file = open("dictionary.txt","r")
tempd= file.read()
wordlist = tempd.split("\n")
wordlist.sort()
rand = random.randint(0,len(wordlist)-1)
wordanddef = wordlist[rand]
locstar = wordanddef.index("*")
solution = []
solution.append(wordanddef[0:locstar])
solution.append(wordanddef[locstar + 1:])

#************************************* CANVAS IMAGE *********************************
canvas = tk.Canvas(root, width = 800, height = 490)
canvas.grid(row = 0, column = 3, columnspan = 6, rowspan = 15)
photo = tk.PhotoImage(file = 'background.png')
canvas.create_image(0,0, image=photo, anchor=tk.NW)
drawCanvas()

#************************************* EXECUTION CODE *********************************
guessed = [] #The list of guessed letters by the user
answer = [] #The string shown to the user
canswer = [] #The actual answer of the word
xshift = [50] #Space between "__"

for i in range (0, len(solution[0]),1):
	canswer.append(solution[0][i])
for i in range (0, len(canswer),1):
	answer.append("__")

root.bind("<Key>",keypressed)

#****************************** lives **********************
life = int(10)
canvas.create_text(624, 355, anchor="nw", text= life)


#************************************* SIDE WIDGETS *********************************
#Menu Button
btnStat1 = tk.Button(root, text = "Menu", font= font, padx = 50, relief = tk.RAISED)
btnStat1.grid(row = 0, column = 0, stick = "NESW", columnspan = 2, padx = 14 ,pady = (14,7))

btnStat1.bind("<Enter>", on_enter)
btnStat1.bind("<Leave>", on_leave)

#Settings Button
btnsettings = tk.Button(root, text = "Settings", command=settings)
btnsettings.grid(row = 1, column = 0, stick = "NESW", columnspan = 2, padx = 14 ,pady = (7,7))

#Vocabulary Button
btnStat3 = tk.Button(root, text = "Vocabulary", command = vocab)
btnStat3.grid(row = 2, column = 0, stick = "NESW", columnspan = 2, padx = 14 ,pady = (7,14))

#New Word Button
btnStat4 = tk.Button(root, text = "New Word", command = generateNewWord)
btnStat4.grid(row = 3, column = 0, stick = "NESW", columnspan = 2, padx = 14 ,pady = (45,14))

#Instructions Box
instr = tk.Text(root, width = 10, height = 7, background = 'grey90')
instr.grid(row = 14, column = 0, columnspan = 2, stick = "NESW", padx = 7 ,pady = 14)
instruction = 1
if instruction == 1:
	text = ("Hello, welcome to WordHang! Look at the definition and try to guess the word.   Just type the guessed letters on your keyboard!")
instr.insert(tk.INSERT, text)
instr.config(state="disabled")

root.mainloop()