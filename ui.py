from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white", font=("Ariel", 10))
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="", width=280, fill="black",
                                                     font=("Ariel", 20, "italic"))
        self.initialize_interface()

    def initialize_interface(self):
        self.window.title("Quizzer")
        self.window.config(height=500, width=300, padx=20, pady=20, bg=THEME_COLOR)

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label.grid(column=1, row=0)

        # Create buttons
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.method_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.method_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def method_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def method_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        self.canvas.configure(bg="green") if is_right else self.canvas.configure(bg="red")
        self.update_score(is_right)
        self.window.after(1000, self.get_next_question)

    def update_score(self, is_right: bool):
        if is_right:
            self.score += 1
        self.score_label.config(text=f"Score: {self.score}")