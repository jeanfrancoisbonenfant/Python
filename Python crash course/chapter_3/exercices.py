
#exercice 3-4 Guest List
from math import ceil, floor


guess = ["brigitte", "danielle", "louka"]

for index in range(len(guess)):
    print(f"\nIt would be an honor {guess[index].title()} if you would accept my invitation for diner.")
        
#exercice 3-5 Changing Guest list
absente = guess.pop(-1)
print(f"\nWe are sorry to hear that you can't make it {absente.title()}.")

guess.append("louise")

for index in range(len(guess)):
    print(f"\nThis is a confirmation for tommorow's diner to the attention of {guess[index].title()}.")
    
#exerice 3-6 More Guests
print()
print("Seems like Brigitte found a bigger table so we will invite more person!!!")

#insert new guess at index[0]
guess.insert(0,"wilbrod")

#find middle of list than insert middle position
middle = ceil((len(guess)/2))
guess.insert(middle, "trevor")
#append guess last index
guess.append("monique")

#loop through new guess list to send invite
for index in range(len(guess)):
    print(f"\n{guess[index].title()} have been invited to our diner tommorow evening")

#exercice 3-7 Shrinking Guest List
print()
print("Sorry for the inconvinient but we won't have space for everyone after all.")

#new list to be removed from initial list
uninvited = ["wilbrod", "trevor", "louise", "danielle"]

#sort list for comparation
guess = sorted(guess)
uninvited = sorted(uninvited)

#loop through both list to remove uninvited guess
for index in range(len(uninvited)):
    #if statement to breakout of 2nd loop when no more to remove
    if index < (len(guess)):
        for i in range(len(uninvited)):
            if uninvited[i] == guess[index]:
                apologize = guess.pop(index)
                print(f"\nSorry {apologize.title()} we won't have enough room for you.")
    else:
        
    #loop through remaining guess to invite them
        for y in range(len(guess)):
            print(f"\nYou have been officially invited {guess[y]}.")          
#congradulation!!
print("\n")
print("I won!!!")

#make list empty & print it
guess.clear()
print(guess)