from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/Words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="french", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_image, image=back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/Words_to_learn.csv", index=False)

    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=10, pady=10, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=900, height=575, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(450, 300, image=front_img)
card_title = canvas.create_text(450, 130, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(450, 275, text="word", font=("Ariel", 40, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

image_wrong = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=image_wrong, highlightthickness=0, command=next_card)
unknown_btn.grid(row=1, column=0)

image_right = PhotoImage(file="images/right.png")
known_btn = Button(image=image_right, highlightthickness=0,command=next_card)
known_btn.grid(row=1, column=1)

next_card()

window.mainloop()