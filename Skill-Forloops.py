import tkinter as tk

def enter:
	output.insert(tk.INSERT,text=("When we think of a for loop I want you to think about: Count (Variable that holds the count), Check: (The check that is done each time the loop runs), Change (The change applied to the count each time the loop runs."))
root = tk.Tk()
root.title("For Loop Notes")

btn = tk.Button(root, text="Enter", command=enter)
btn.pack(pady = 10, padx = 10)

output = tk.Text(root, width=40, height=10, borderwidth=7, relief=tk.GROOVE)
output.pack()

root.mainloop()