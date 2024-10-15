import random

class fruitquiz:
    def __init__(self):
        self.fruit= {'apple':'red',
                     'orange':'orange',
                     'watermelon':'green',
                     'lemon':'yellow'}
        
    def quiz(self):
        while True:
            fruit, color=random.choice(list(self.fruit.items()))
            print("What is the color of {}".format(fruit))
            user_answer = input()
            
            if(user_answer.lower() == color):
                print("Correct Answer.")

            else:
                print("Wrong Answer.")

            option = int(input("Do you want to continue? \n If yes then 1 else 0"))
            if(option):
                break

fq = fruitquiz()
fq.quiz()