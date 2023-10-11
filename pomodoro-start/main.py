from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    tick.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec= LONG_BREAK_MIN * 60
    if reps == 0 or reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="WORK", font=("Arial", 30, "italic"), bg=YELLOW, fg=GREEN)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="SHORT BREAK", font=("Arial", 30, "italic"), bg=YELLOW, fg=PINK)

    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="LONG BREAK", font=("Arial", 30, "italic"), bg=YELLOW, fg=RED)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        tick.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.minsize(width=500, height=500)
window.config(padx=90, pady=100, bg=YELLOW)



timer_label = Label(text="Timer", font=("Arial", 30, "italic"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


start_button = Button(text="Start", font=("Arial", 12, "italic"), bg=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

tick = Label(font=("Arial", 12, "italic"), bg=YELLOW, fg=GREEN)
tick.grid(row=3, column=1)

stop_button = Button(text="Reset", font=("Arial", 12, "italic"), bg=YELLOW, command=reset_timer)
stop_button.grid(row=2, column=2)

window.mainloop()