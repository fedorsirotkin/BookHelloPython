from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=925, height=628)
canvas.pack()

space = PhotoImage(file="images/space.gif")
canvas.create_image(0, 0, anchor=NW, image=space)

tk.mainloop()
