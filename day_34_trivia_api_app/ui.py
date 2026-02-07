THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
from pathlib import Path
import time

BASE_DIR = Path(__file__).resolve().parent
from enum import Enum, auto

class State(Enum):
    QUESTION = auto()
    FINISHED = auto()

class QuizUI():
    def __init__(self, brain: QuizBrain):
        self.brain = brain
        self.state = State.QUESTION

        # Window
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        # Score
        self.score_label = Label(text=f"Score: {self.brain.score}", fg="white", font=("Arial", 15, "normal"), bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(row=0, column=1)
        
        # Question canvas
        self.question_canvas = Canvas(self.window,height=250, width=300, bg="white", highlightthickness=0)
        self.question_canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.question_text = self.question_canvas.create_text(
            150, 125,  # center for a 300x250 canvas
            text="Some Question Text.",
            fill=THEME_COLOR,
            font=("Arial", 15, "italic"),
            width=280  # optional: wrap text
        )
        
        # True button
        self.true_button_img = PhotoImage(file=str(BASE_DIR / "images" / "true.png"))
        self.true_button = Button(image=self.true_button_img, highlightthickness=0, command=lambda: self.answer_question('true'))
        self.true_button.grid(row=2, column=0, pady=(20, 0))
        
        # False button
        self.wrong_button_img = PhotoImage(file=str(BASE_DIR / "images" / "false.png"))
        self.false_button = Button(image=self.wrong_button_img, highlightthickness=0, command=lambda: self.answer_question('false'))
        self.false_button.grid(row=2, column=1, pady=(20, 0))

        self.next_question()
        self.window.mainloop()
        
    def next_question(self):
        if not self.brain.still_has_questions():
            self.state = State.FINISHED
            self.question_canvas.itemconfig(
                self.question_text, text="Start new game?",
            )
        
        self.enable_buttons()
        self.question_canvas.config(bg="white")
        
        if self.state == State.QUESTION:
            question = self.brain.next_question()
            self.question_canvas.itemconfig(self.question_text, text=question)
        
    def enable_buttons(self):
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")
        
    def disable_buttons(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        
    def answer_question(self, user_answer: str):
        if self.state == State.QUESTION:
            if self.brain.check_answer(user_answer):
                self.question_canvas.config(bg="green")      
            else:
                self.question_canvas.config(bg="red")
            
            self.disable_buttons()
            self.window.after(500, self.next_question)
            self.score_label.config(text=f"Score: {self.brain.score}")
            
        if self.state == State.FINISHED:
            print(user_answer)
            if user_answer.lower() == 'true':
                self.brain = QuizBrain()
                self.state = State.QUESTION
                self.next_question()
            elif user_answer.lower() == 'false':
                self.window.destroy()
            