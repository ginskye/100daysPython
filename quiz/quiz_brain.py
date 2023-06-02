class QuizBrain:

    def __init__(self, quiz_list):
        self.q_num = 0
        self.q_list = quiz_list
        self.score = 0

    def more_quest(self):
        if self.q_num < len(self.q_list):
            return True
        else:
            print("Game Over!")
            return False

    def check_answer(self, answer, current_question):
        if answer.lower()==current_question.lower():
            self.score +=1
            print(f"Correct! Your score is {self.score}")
        else:
            print(f"Sorry, that's not right!\nThe correct answer was: {current_question}")
        print(f"Your current score is {self.score}/{self.q_num}")

    def next_q(self):
        curr_quest = self.q_list[self.q_num]
        self.q_num += 1
        answ = input(f"Q{self.q_num}: {curr_quest.text} (True/False): ")
        self.check_answer(answ, curr_quest.answer)

