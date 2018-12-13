# import the tkinter tooklbox with many preset stuff that i could use
import tkinter as tk

def enter():
	print (entPassword)
	print (entUN)
#with the login page all elements are vertically aligned
#So therefore only pack is needed, no grid coordinates

#Main window
root = tk.Tk() 
#.Tk() generates the standard window in the tkinter toolbox
#Tk is a special function called a CONSTRCTER. 
#If a function is written with a capital leter and it indicates it is a constructer


#********************* WIDGET BUILDING ***************
#THree stanges to build elements/objects:
#1. Construct the object. We build and configure it
#2. Configure the object. We specify behaviours and setting (optional)
#3. pack the object so it shows in the window

labUN = tk.Label(root, text = "User Name")
#ordered parameters: the order we send them matters (COMMON)
#named parameters: JavaScript and python specific
#We look up on google for the millions of parameters that can be used...
labUN.pack()

entUN= tk.Entry(root)
entUN.pack(padx = 15, pady = 15)

labPassword=tk.Label(root, text = "Password")
labPassword.pack()

entPassword = tk.Entry(root, show = "*")
entPassword.pack(padx = 15, pady = 15)

entBtn = tk.Button(root, text = "Login", command=enter)
entBtn.pack()




#We are writing an EVENT DRIVEN PROGRAM
# Build the GUI, start it running, Wait for "Event"
root.mainloop() #Starts the program