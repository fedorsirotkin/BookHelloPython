from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=400, height=400)
canvas.pack()

canvas.create_line(0, 0, 400, 400)

tk.mainloop()
