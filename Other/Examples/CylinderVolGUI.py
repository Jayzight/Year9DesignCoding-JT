import tkinter as tk
import math

def enter():
	#print ("THE BUTTON IS PRESSED!")
	r = float(entr.get())
	r = r/2
	s = math.pi*r**3*4/3
	s = round(s,3)

	output.insert(tk.INSERT,s)

root = tk.Tk() #'Tk()' consturcts the window
root.title("Jayson's Multiplication Thingy")

labr = tk.Label(root, text="Diameter")
labr.pack(pady = 10)
#Pack is packing it, and pady is putting extra pixels above and below the widget

entr = tk.Entry(root)
entr.pack(pady = 10, padx = 20)
#PadX is putting pixels left and right of the widget

labh = tk.Label(root, text="Number 2")
labh.pack(pady = 10)

enth = tk.Entry(root)
enth.pack(pady = 10, padx = 20)

btn = tk.Button(root, text="Enter", command=enter)
btn.pack(pady = 10, padx = 10)

output = tk.Text(root, width=40, height=10, borderwidth=7, relief=tk.GROOVE)
output.pack()

root.mainloop()