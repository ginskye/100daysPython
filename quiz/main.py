from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
#print(question_data)

for item in question_data:
    q_text = item["question"]
    #print(q_text)
    q_answ = item["correct_answer"]
    #print(q_answ)
    new_quest = Question(q_text, q_answ)
    #print(new_quest.text)
    question_bank.append(new_quest)



game = QuizBrain(question_bank)
while game.more_quest():
    game.next_q()
print(f"Your final score was {game.score} {len(question_bank)}")