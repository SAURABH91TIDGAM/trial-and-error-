from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a label", font=("Arial", 24, "bold", "italic"))
my_label.pack(side="left")

my_label["text"] = "New Text"
my_label.config(text="New Text")

button = Button()

window.mainloop()
