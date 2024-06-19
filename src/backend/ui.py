from tkinter import *

window = Tk()
window.geometry("800x600")
window.resizable(width=False, height=False)
greeting = Label(window, text="Hello, Tkinter")
greeting.grid(row=0, column=0)
test = Label(window, text="test")
test.grid(row=1, column=1)

window.mainloop()