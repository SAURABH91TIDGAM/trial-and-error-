from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)


my_label = Label(text="I am a label", font=("Arial", 24, "bold", "italic"))
my_label.grid(column=0, row=0)
#my_label.pack(side="top")


my_label["text"] = "New Text"
my_label.config(text="one")

input = Entry()

def button_clicked():
    # print("I got clicked")

   my_label.config(text=input.get())


button = Button(text="print text", command=button_clicked)
input.grid(column=4, row=4)
# button.pack()
button.grid(column=3, row=3)


#Entry

input = Entry()
# input.pack()
# print(input.get())



window.mainloop()
