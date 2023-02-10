from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT =("Arial", 20, "italic")
FONT1 =("Arial", 10, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzz!")
        # self.window.geometry("600x400+50+50")
        self.window.config(bg=THEME_COLOR)
        self.window.resizable(False, False)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Hello",
            font=FONT,
            fill=THEME_COLOR
        )
        self.canvas.grid(columnspan=2, column=0, row=1, padx=20, pady=20)

        self.score = Label(text="Score: ", font=FONT1, bg=THEME_COLOR, bd=0, highlightthickness=0, fg="white")
        self.score.grid(column=1, row=0, pady=20, padx=5)

        self.ok_button_img = PhotoImage(file="./images/true.png")
        self.ok_button = Button(image=self.ok_button_img, width=100, height=97, bd=0 , highlightthickness=0)
        self.ok_button.grid(column=0, row=2, pady=20)

        self.wrong_button_img = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=self.wrong_button_img, width=100, height=97, bd=0, highlightthickness=0)
        self.wrong_button.grid(column=1, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

