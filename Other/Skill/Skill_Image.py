import tkinter as tk
root = tk.Tk() #'Tk()' consturcts the window
root.title("Image")

canvas = tk.Canvas(root)
canvas.pack()
image1= tk.PhotoImage(file='IMG_2549.png')
canvas.create_image(0,0, anchor= tk.NW, image=image1)
canvas.create_line(10,10,100,100, fill = "red")
canvas.create_rectangle(10,10,50,50,fill = "red")
root.mainloop()