import html
from data import get_quiz_data
from question_model import Question

import html
from data import get_quiz_data
from question_model import Question

class QuizBrain:
    def __init__(self):
        self.question_number = 0
        self.score = 0
        self.current_question = None
        self.question_list = []
        self.reset_with_new_data()

    def reset_with_new_data(self):
        self.question_number = 0
        self.score = 0
        self.current_question = None

        self.question_list = []
        for q in (get_quiz_data() or []):
            self.question_list.append(Question(q["question"], q["correct_answer"]))

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer: str) -> bool:
        correct_answer = self.current_question.answer
        is_right = user_answer.lower() == correct_answer.lower()
        if is_right:
            self.score += 1
        return is_right
