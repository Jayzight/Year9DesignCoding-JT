import tkinter as tk

def changeStateContrast(*args):
	print("Change Contrast")
	print(var1.get())
	if var1.get() == 1:
		root.config(bg = "black")
		cbox1.config(bg = "black", fg = "yellow")
		cbox2.config(bg = "black", fg = "yellow")
	if var1.get() == 0:
		root.config(bg = "white")
		cbox1.config(bg = "white",fg = "black")
		cbox2.config(bg = "white",fg = "black")

def changeStateFont(*args):
	print("changed font")
	print(var1.get())
	if var2.get() == 1:
		cbox1.config(font=("Courier", 44))
		cbox2.config(font=("Courier", 44))

	if var2.get() == 0:
		cbox1.config(font=("Courier", 20))
		cbox2.config(font=("Courier", 20))

#create main window
root = tk.Tk()

#An IntVar is a special variable that we "link" to an element
#as we change the element the IntVar will toggle between values
#in this case it will go between 0 (no check) and 1 (check)
var1 = tk.IntVar()
#Creates our checkbox element
cbox1 = tk.Checkbutton(root, text="High Contrast", variable=var1)
#configure the font type and size
cbox1.config(font=("Courier", 20))
#Tracing a var like this means that we can run a function
#when something happens.  The "w" means that when the 
#variable is written to, changed, we will run the changeStateContrast
#function. The change is automatically made when the checkbox is selected
#since we have linked var1 to cbox1
var1.trace("w",changeStateContrast)
#We have packed the cbox into the root.  Including the named parameter
#fill = "both" means the two checkboxs will have the same dimensions meaning
#
cbox1.pack(fill = "both")

var2 = tk.IntVar()
cbox2 = tk.Checkbutton(root, text="Large Font", variable=var2)
cbox2.config(font=("Courier", 20))
var2.trace("w",changeStateFont)
cbox2.pack(fill = "both")






root.mainloop()