from random import choice

lottery = (1, 2, 3 , 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E")
winner = ""
for i in range(4):
    winner += str(choice(lottery))
print(f"\nThe winning ticket is : {winner}")