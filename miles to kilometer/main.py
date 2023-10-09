from tkinter import *

window = Tk()
window.title("Miles to kilometer Converter")
window.minsize(width=360, height=200)
window.config(padx=20, pady=20)

distance_input = Entry(width=20)
distance_input.grid(row=0, column=1)


def convert():
    miles = float(distance_input.get())
    km = miles * 1.609
    result_label.config(text=km)


miles = Label(text="Miles", font=("Arial", 24, "bold", "italic"))
miles.grid(row=0, column=2)
xfyxgjngxhvn  vvvb

equal_to = Label(text="is equal to", font=("Arial", 12, "italic"))
equal_to.grid(row=1, column=0)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

kilometer = Label(text="Kilometer", font=("Arial", 14, "italic"))
kilometer.grid(row=1, column=2)

button =  Button(text="Convert", command=convert)
button.grid(row=2, column=1)




window.mainloop()
