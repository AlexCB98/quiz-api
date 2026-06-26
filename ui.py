from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'normal')

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quiz-API')
        self.window.minsize(width=500, height=700)
        self.window.config(bg=THEME_COLOR)
        self.window.grid_columnconfigure(0, weight=1, uniform="columns")
        self.window.grid_columnconfigure(1, weight=1, uniform="columns")

        self.label = Label(text='Score: 0',
                           font = FONT,
                           bg=THEME_COLOR,
                           fg='white')
        self.label.config(padx=50, pady=20)
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=450, height=400,
                             bg='white')
        self.question_text = self.canvas.create_text(
            225, 200,
            width=430,
            text='Question',
            fill=THEME_COLOR,
            font=FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2,
                         padx=25, pady=25)

        true_img  = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')

        self.true_button = Button(
            image=true_img,
            highlightthickness=0,
            borderwidth=0,
            command=self.true_check
        )
        self.true_button.grid(row=2, column=0, padx=20)

        self.false_button = Button(
            image=false_img,
            highlightthickness=0,
            borderwidth=0,
            command=self.false_check
        )
        self.false_button.grid(row=2, column=1, padx=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')

        if self.quiz.still_has_questions():
            self.label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text="You've reached the end of the quiz."
            )
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')


    def true_check(self):
        is_right = self.quiz.check_answer('True')
        self.feedback(is_right)

    def false_check(self):
        is_right = self.quiz.check_answer('False')
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)