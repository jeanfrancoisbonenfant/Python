from random import randint

class Die:
    """ Initialize Dice """
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        """ Generate random roll with dice face high """
        winner = randint(1,self.sides)
        print(f"You pulled a {winner}!")

""" Create 3 dice instance for trial """
dice = Die(6)
print("Six face dice: ")
for i in range(10):
    dice.roll_die()

ten_face = Die(10)
print("Ten face dice: ")
for i in range(10):
    ten_face.roll_die()

twenty_face = Die(20)
print("Twenty face dice: ")
for i in range(10):
    twenty_face.roll_die()