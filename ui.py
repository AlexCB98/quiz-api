from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title('Quiz-API')
        self.window.minsize(width=500, height=700)
        self.window.config(bg=THEME_COLOR)

        self.label = Label(text='Score: 0',
                           font = ("Arial", 20, "normal"),
                           bg=THEME_COLOR,
                           fg='white')
        self.label.config(padx=50, pady=20)
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=450, height=400,
                             bg='white')
        self.canvas.grid(row=1, column=0, columnspan=2,
                         padx=25, pady=25)


        



        self.window.mainloop()