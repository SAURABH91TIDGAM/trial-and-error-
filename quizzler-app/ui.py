import tkinter
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=30, pady=40, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Ariel", 20, "italic"))
        self.score_label.grid(row=0, column=1)
        self.win_canvas = Canvas(width=400, height=400, highlightthickness=0)
        self.question_text = self.win_canvas.create_text(
            200,
            200,
            width=200,
            text="Some text",
            fill=THEME_COLOR, font=("Ariel", 24, "italic"))
        self.win_canvas.grid(row=1, column=0, columnspan=2, pady=20)

        tick_image = PhotoImage(file=  "images/true.png")
        cross_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=tick_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=cross_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.win_canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.win_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have completed the Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.win_canvas.config(bg="green")
        else:
            self.win_canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
