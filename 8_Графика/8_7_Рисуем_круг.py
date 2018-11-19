from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=200, height=200)
canvas.pack()

canvas.create_oval(10, 10, 90, 90)

tk.mainloop()
