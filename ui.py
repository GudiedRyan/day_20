from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: 0", fg="white", font=("Arial", 12), bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150,125, width=280, text="", font=("Arial", 20, "italic"), fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_img, highlightthickness=0, borderwidth=0, command=self.check_true_answer)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_img, highlightthickness=0, borderwidth=0, command=self.check_false_answer)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text) 
        else:
            self.canvas.itemconfig(self.question, text=f"You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true_answer(self):
        self.give_feedback(is_right = self.quiz.check_answer("true"))

    def check_false_answer(self):
        self.give_feedback(self.quiz.check_answer("false"))


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)