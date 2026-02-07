from question_model import Question
from data import get_quiz_data
from quiz_brain import QuizBrain
from ui import QuizUI

brain = QuizBrain()
quiz_ui = QuizUI(brain)
