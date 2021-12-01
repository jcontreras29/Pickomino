"""
    # This is the simulation of the game Pickomino
    # Joseph Contreras
"""


from random import *
import operator
from time import sleep


beast0319 = []
opposition = []

def pickomino(beast0319):
    rounds = 0
    dice = [1, 2, 3, 4, 5, 'Worm']
    keepRunning = True
    onTable = 8
    total = 0
    keepers = []
    while keepRunning:
        keepRunning2 = True
        if (len(keepers) == 8 and 'Worm' in keepers):
            print("My total is",total,"...nice round!")
            beast0319 = addBeastlyScore(beast0319, total)
            break
        elif (len(keepers) == 8 and not('Worm' in keepers)):
            total = 0
            print("I've busted.")
            beast0319 = addBeastlyScore(beast0319, total)
            break
        for i in range(onTable):
            roll = [choice(dice) for i in range(onTable)]
        rounds += 1
        #playGame = input("Would you like to roll: (Y/N)")
        if (yesOrNoAlg(keepers, total, beast0319, opposition)):
            print("This is what I rolled: ",roll)
            sleep(1)
            print("These are the dice I've kept so far: ",keepers)
            sleep(1)
            if (bustCheck(roll, keepers)):
                total = 0
                print("I busted and cannot roll again. 0 points!")
                beast0319 = addBeastlyScore(beast0319, total)
                break
            while keepRunning2:
                collect = collectionAlg(roll, keepers, rounds)
                if (collect == 'worm' or collect == 'Worm'):
                    if ('Worm' in keepers):
                        print("I've already collected this try a again.")
                    elif ('Worm' not in roll):
                        print("I cannot collect this it was not rolled.")
                    else:
                        for i in roll:
                            if (i == 'Worm'):
                                keepers.append(i)
                                total += 5
                                onTable -= 1
                        print("Here is what I've collected", keepers)
                        print("I now have",total,"points")
                        keepRunning2 = False
                else:
                    collect = int(collect)
                    if (collect in keepers):
                        print("I've already collected this try again.")
                    elif (collect not in roll):
                        print("I cannot collect this it was not rolled.")
                    else:
                        if (collect == 1):
                            for i in roll:
                                if (i == 1):
                                    keepers.append(i)
                                    total += i
                                    onTable -= 1
                            print("I are the dice I've kept: ",keepers)
                            sleep(1)
                            print("This is my score at the moment: ", total)
                            sleep(1)
                            keepRunning2 = False
                        elif (collect == 2):
                            for i in roll:
                                if (i == 2):
                                    keepers.append(i)
                                    total += i
                                    onTable -= 1
                            print("I are the dice I've kept: ",keepers)
                            sleep(1)
                            print("This is my score at the moment: ", total)
                            sleep(1)
                            keepRunning2 = False
                        elif (collect == 3):
                            for i in roll:
                                if (i == 3):
                                    keepers.append(i)
                                    total += i
                                    onTable -= 1
                            print("These are the dice I've kept: ",keepers)
                            sleep(1)
                            print("This is my score at the moment: ", total)
                            sleep(1)
                            keepRunning2 = False
                        elif (collect == 4):
                            for i in roll:
                                if (i == 4):
                                    keepers.append(i)
                                    total += i
                                    onTable -= 1
                            print("These are the dice I've kept: ",keepers)
                            sleep(1)
                            print("This is my score at the moment: ", total)
                            sleep(1)
                            keepRunning2 = False
                        elif (collect == 5):
                            for i in roll:
                                if (i == 5):
                                    keepers.append(i)
                                    total += i
                                    onTable -= 1
                            print("These are the dice I've kept: ",keepers)
                            sleep(1)
                            print("This is my score at the moment: ", total)
                            sleep(1)
                            keepRunning2 = False
                        else:
                            print("Please enter a valid number.")
        else:
            if ('Worm' in keepers):
                print(total," points is my score for the round!")
                sleep(1)
                beast0319 = addBeastlyScore(beast0319, total)
                keepRunning = False
            else:
                total = 0
                print("I could not cash out because I did not have a worm.")
                sleep(1)
                print("I will receive 0 points.")
                beast0319 = addBeastlyScore(beast0319, total)
                keepRunning = False


def bustCheck(rolled, kept):
    total = 0
    amount = len(rolled)
    for i in rolled:
        if (i in kept):
            total += 1
    if (total == amount):
        return True
    else:
        return False



# This function should return what we want to collect considering circustances
# Should return a number from 1-5 or 'Worm'
def collectionAlg(rolled, kept, rounds):
    worms = 0 
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    ofAKind = 0
    diceKept = 0
    # This step right here counts each amount that of what we collected so far
    for i in rolled:
        if (i != 'Worm'):
            i = int(i)
            if (i == 1):
                ones += 1
                diceKept += 1
            elif (i == 2):
                twos += 2
                diceKept += 1
            elif (i == 3):
                threes += 3
                diceKept += 1
            elif (i == 4):
                fours += 4
                diceKept += 1
            elif (i == 5):
                fives += 5
                diceKept += 1
        elif (i == 'Worm'):
            worms += 5
            diceKept += 1
    
    weights = {"worms":worms,
               "ones":ones,
               "twos":twos,
               "threes":threes,
               "fours":fours,
               "fives":fives}
    if (rounds == 1):
        weights = {"worms":worms*(1.8),
               "ones":ones*(.5),
               "twos":twos*(.6),
               "threes":threes*(.8),
               "fours":fours*(1.1),
               "fives":fives*(1.4)}
    elif (rounds == 2):
        weights = {"worms":worms*(1.85),
               "ones":ones*(.7),
               "twos":twos*(.8),
               "threes":threes*(.9),
               "fours":fours*(1.1),
               "fives":fives*(1.3)}
    elif (rounds == 3):
        weights = {"worms":worms*(2),
               "ones":ones*(.72),
               "twos":twos*(.87),
               "threes":threes*(1),
               "fours":fours*(1.19),
               "fives":fives*(1.35)}
    elif (rounds == 4):
        weights = {"worms":worms*(2.5),
               "ones":ones*(.75),
               "twos":twos*(.92),
               "threes":threes*(1),
               "fours":fours*(1.3),
               "fives":fives*(1.65)}
    elif (rounds == 5):
        weights = {"worms":worms*(3),
               "ones":ones*(.76),
               "twos":twos*(.93),
               "threes":threes*(1),
               "fours":fours*(1.4),
               "fives":fives*(1.8)}
    elif (rounds == 6):
        weights = {"worms":worms*(3.2),
               "ones":ones*(.8),
               "twos":twos*(.95),
               "threes":threes*(1),
               "fours":fours*(1.6),
               "fives":fives*(1.95)}
    elif (rounds == 7):
        weights = {"worms":worms*(3.5),
               "ones":ones*(1),
               "twos":twos*(1),
               "threes":threes*(1),
               "fours":fours*(1.85),
               "fives":fives*(2)}
    
    
    if ('Worm' in kept):
        weights["worms"] = 0
    if (1 in kept):
        weights["ones"] = 0
    if (2 in kept):
        weights["twos"] = 0
    if (3 in kept):
        weights["threes"] = 0
    if (4 in kept):
        weights["fours"] = 0
    if (5 in kept):
        weights["fives"] = 0

    
    largest = max(weights.items(), key=operator.itemgetter(1))[0]
    if (largest == 'worms'):
        return 'Worm'
    elif (largest == 'ones'):
        return int(1)
    elif (largest == 'twos'):
        return int(2)
    elif (largest == 'threes'):
        return int(3)
    elif (largest == 'fours'):
        return int(4)
    elif (largest == 'fives'):
        return int(5)
        
               
    
    

# This function will return whether we want to roll or not
# True - Yes we want to roll
# False - No we do not want to roll
def yesOrNoAlg(kept, total, beast0319, opposition):
    worms = 0
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    ofAKind = 0
    diceKept = 0
    # This step right here counts each amount that of what we collected so far
    for i in kept:
        if (i != 'Worm'):
            i = int(i)
            if (i == 1):
                ones += 1
                diceKept += 1
            elif (i == 2):
                twos += 1
                diceKept += 1
            elif (i == 3):
                threes += 1
                diceKept += 1
            elif (i == 4):
                fours += 1
                diceKept += 1
            elif (i == 5):
                fives += 1
                diceKept += 1
        elif (i == 'Worm'):
            worms += 1
            diceKept += 1
            
    # Determine how many of a kind we have
    keptSet = set(kept)
    repeats = len(keptSet)
    slotsRemaining = 8 - diceKept

    # Right here is where we start making decisions
    # if something goes wrong check to see if four of a repeat and the 3choose2 possibility is right
    if (worms == 0):
        return True
    elif (total in beast0319):
        return True
    elif (total in opposition):
        opposition = removeOpp(opposition, total)
        return False
    elif (total < 21):
        return True
    elif (repeats <= 3 and slotsRemaining >= 2 and total <= 32): 
        return True
    elif (repeats == 4 and slotsRemaining == 1 and ((threes == 0 and fours == 0) or (threes == 0 and fives == 0) or (fours == 0 and fives == 0))):
        return True
    elif (repeats == 4 and slotsRemaining >= 2  and (fives == 0 and fours == 0)):
        return True
    elif (repeats == 5 and slotsRemaining == 2 and (fives == 0 or fours == 0)):
        return True
    elif (repeats == 5 and slotsRemaining >= 3):
        return True
    else:
        return False


def addBeastlyScore(beast0319, score):
    if (score >= 21 and score <= 36):
        beast0319.append(score)
    return beast0319

def removeOpp(opposition, score):
    if (int(score) in opposition):
        opposition.remove(int(score))
    return opposition

_round = 1

while True:
    print("Round",_round)
    print("My dominoes:",beast0319)
    print("Your dominoes:",opposition)
    player1 = input("Enter your score or 'quit': ")
    if (str(player1) == 'quit'):
        print("Thanks for playing!")
        break
    elif (str(player1) != 'quit'):
        if (int(player1) >= 21 and int(player1) <= 36 and int(player1) not in opposition):
            opposition.append(int(player1))
        if (int(player1) in beast0319):
            beast0319.remove(int(player1))
        pickomino(beast0319)
    _round+=1
