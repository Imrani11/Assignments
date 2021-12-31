import random
class Flashcard:
    def __init__(self):
        self.quiz = {'apple':'fruit','rx100':'bike','rajamouli':'director','alluarjun':'actor','einstein':'scientist'}
    def ask(self):
        print("'welcome to fruit quiz' ")
        while(True):
           que = random.choice(list(self.quiz.keys()))
           print('what is {} ?'.format(que))
           user = input('enter your answer :')
           if user.lower() == self.quiz[que]:
               print('you are right')
           else:
               print('wrong answer')
           play = int(input('enter 1 if you want to continue :'))
           if not (play):
               break


# palindrome number
def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False

f = Flashcard()
f.ask()