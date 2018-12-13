import tkinter as tk

LARGE_FONT= ("Verdana", 20)


def enter():
    root2 = tk.Tk()
   



root = tk.Tk() #'Tk()' consturcts the window
root.title("Windows")

labr = tk.Label(root, text="A NEW WINDOW", font=LARGE_FONT)
labr.pack(pady = 30, padx = 30)

btn = tk.Button(root, text="Open New Window", command=enter)
btn.pack(pady = 30, padx = 30)



root.mainloop()
           