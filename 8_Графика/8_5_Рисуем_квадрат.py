from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=400, height=400)
canvas.pack()

canvas.create_rectangle(20, 20, 360, 360)

tk.mainloop()
