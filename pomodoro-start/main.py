from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.minsize(width=500, height=500)
window.config(padx=90, pady=100, bg=YELLOW)

timer = Label(text="Timer", font=("Arial", 30, "italic"), bg=YELLOW, fg=GREEN)
timer.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start = Label(text="Start", font=("Arial", 12, "italic"), bg=YELLOW)
start.grid(row=2, column=0)

tick = Label(text="✔", font=("Arial", 12, "italic"), bg=YELLOW, fg=GREEN)
tick.grid(row=3, column=1)

stop = Label(text="Stop", font=("Arial", 12, "italic"), bg=YELLOW)
stop.grid(row=2, column=2)

window.mainloop()