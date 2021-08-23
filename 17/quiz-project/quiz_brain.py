class QuizBrain:
    def __init__(self, questions_list):
        self.questions_number = 0
        self.questions_list = questions_list
        self.score = 0


def still_has_questions(self):

    questions_left = len(self.questions_list) - self.questions_number
    if questions_left == 0:
        return False
    else:
        return True


def next_question(self):
    current_question = self.questions_list[self.questions_number]
    self.questions_number += 1
    
    answer = ""
    while answer != "True" and answer != "False":
        answer = input(f"Q.{self.questions_number} - {current_question.text} True/False: ").title()
        print(answer)

    if answer == current_question.answer:
        self.score += 1
        print(f"Correct answer! Score: {self.score}")
    else:
        print(f"Incorrect answer! Score: {self.score}")

    while still_has_questions(self) is True:
        next_question(self)
