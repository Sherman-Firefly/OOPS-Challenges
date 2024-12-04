import math
import random

class Fruit_Quiz:
    def __init__(self):
        self.fruits={'apple' : 'red', 'orange':'orange', 'banana':'yellow','grape':'purple'}

    def quiz(self):
        while True:
            fruits,colors=random.choice(list(self.fruits.items()))
            print("Welcome to the fruit quiz.")
            print("Choose red, orange, yellow, or purple to answer")
            print("What is the color {}".format(fruits))
            user=input()
            if (user.lower()==colors):
                print("Correct!")
            else:
                print("Wrong!")

            option=input("Enter 0 if you want to play again; enter to quit")
            if(option):
                break
        

print("Fruit quiz time!")
fq=Fruit_Quiz()
fq.quiz()


