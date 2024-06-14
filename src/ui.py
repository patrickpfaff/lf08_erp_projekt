import tkinter as tk

window = tk.Tk()
window.geometry("800x600")
window.resizable(width=False, height=False)
greeting = tk.Label(text="Hello, Tkinter")

greeting.pack()

window.mainloop()