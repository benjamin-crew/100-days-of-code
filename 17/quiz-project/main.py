from question_model import Question
from data import question_data
from quiz_brain import QuizBrain, next_question


question_bank = []
for question in question_data:

    question_obj = Question(question["text"], (question["answer"]))
    question_bank.append(question_obj)

quiz = QuizBrain(question_bank)
next_question(quiz)

print("There are no questions left.")
print(f"Final score: {quiz.score}")