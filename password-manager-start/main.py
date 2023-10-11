from tkinter import *
import math
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(width=600, height=500)
window.config(padx=20, pady=20)

canvas = Canvas(width=300, height=300, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(160, 180, image=logo_img)

canvas.pack()

window.mainloop()