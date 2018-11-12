import tkinter as tk
root = tk.Tk() #'Tk()' consturcts the window
root.title("Image")

canvas = Canvas(root, width = 500, height = 500)
canvas.pack()
image1=PhotoImage(file='Macintosh HD⁩ ▸ ⁨Users⁩ ▸ ⁨jayson.tian⁩ ▸ ⁨Desktop⁩ ▸ ⁨Git Repo⁩ ▸ ⁨Year9DesignCoding-JT⁩ ▸ beautiful.jpg')
canvas.create_image(0,0, anchor=NW, image=image1)