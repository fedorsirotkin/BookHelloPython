from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=150, height=150, bg="blue")
canvas.pack()

canvas.create_oval(10, 10, 90, 90, fill="red", outline="yellow")

tk.mainloop()
