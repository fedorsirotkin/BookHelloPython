from tkinter import *


def hello():
    print("Привет!")


tk = Tk()
btn = Button(tk, text="Нажми", command=hello)
btn.pack()

tk.mainloop()
