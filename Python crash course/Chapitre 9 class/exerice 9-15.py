from random import choice

lottery = (1, 2, 3 , 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E")

jackpot = ""
for i in range(4):
    jackpot += str(choice(lottery))
print(jackpot)
lucky = ""
for i in range(4):
    lucky += str(choice(lottery))
winner = True
count = 0
while winner:
    if  jackpot !=  lucky:
        lucky = ""
        count += 1
        for i in range(4):
            lucky += str(choice(lottery))
    elif jackpot == lucky:
        winner = False
        print(lucky)
        print(f"{count} attempts were required to win...")