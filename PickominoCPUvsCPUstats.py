"""
    # This is the simulation of the game Pickomino
    # Joseph Contreras
"""


from random import *
import operator
from time import sleep


beast0319 = []
opposition = []
_round = 1
beastLength = len(beast0319)


dominoes = [21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
highestDominoe = dominoes[len(dominoes)-1]

def poorBeast(beast0319):
    beast0319.pop()
    return beast0319


def pickomino(beast0319, highestDominoe, dominoes, opposition):
    beastHigh = 0
    if (len(beast0319) > 0):
        for i in beast0319:
            if (int(i) > beastHigh):
                beastHigh = int(i)
    rounds = 0
    dice = [1, 2, 3, 4, 5, 'Worm']
    keepRunning = True
    onTable = 8
    total = 0
    keepers = []
    while keepRunning:
        keepRunning2 = True
        if (len(keepers) == 8 and ('Worm' in keepers)):
            if (total not in dominoes):
                total = 0
                #print("I've busted.")
                dominoes.pop()
                if (len(beast0319) != 0):
                    dominoes.append(beast0319.pop())
                    dominoes.sort()
                else:
                    dominoes.sort()
            else:
                #print("My total is",total)
                beast0319 = addBeastlyScore(beast0319, total, highestDominoe)
                dominoes.remove(total)
                dominoes.sort()
            break
        elif (len(keepers) == 8 and not('Worm' in keepers)):
            total = 0
            #print("I've busted.")
            dominoes.pop()
            if (len(beast0319) != 0):
                dominoes.append(beast0319.pop())
                dominoes.sort()
            else:
                dominoes.sort()
            break
        for i in range(onTable):
            roll = [choice(dice) for i in range(onTable)]
        rounds += 1
        if (yesOrNoAlg(keepers, total, beast0319, opposition, highestDominoe, dominoes)):
            #sleep(1)
            #print("This is what I rolled: ",roll)
            #sleep(1)
            #print("These are the dice I've kept so far: ",keepers)
            #sleep(1)
            if (bustCheck(roll, keepers)):
                total = 0
                #sleep(1)
                #print("I busted and cannot roll again. 0 points!")
                if (len(beast0319) != 0):
                    dominoes.append(beast0319.pop())
                    dominoes.sort()
                dominoes.pop()
                dominoes.sort()
                break
            while keepRunning2:
                collect = collectionAlg(roll, keepers, rounds, opposition, total, dominoes)
                if (collect == 'worm' or collect == 'Worm'):
                    if ('Worm' in keepers):
                        #print("I've already collected this try a again.")
                        total = 0
                        keepRunning2 = False
                    elif ('Worm' not in roll):
                        print("I cannot collect this it was not rolled.")
                    else:
                        for i in roll:
                            if (i == 'Worm'):
                                keepers.append(i)
                                total += 5
                                onTable -= 1
                        #print("Here is what I've collected", keepers)
                        #print("I now have",total,"points")
                        keepRunning2 = False
                else:
                    collect = int(collect)
                    if (collect in keepers):
                        #print("I've already collected this try again.")
                        total = 0
                        #print("I have busted")
                        keepRunning2 = False
                    elif (collect not in roll):
                        print("I cannot collect this it was not rolled.")
                    else:
                        if (collect == 1):
                            for i in roll:
                                if (i == 1):
                                    keepers.append(i)
                                    total += i
                                    onTable -= 1
                            #print("These are the dice I've kept: ",keepers)
                            #sleep(1)
                            #print("This is my score at the moment: ", total)
                            #sleep(1)
                            keepRunning2 = False
                        elif (collect == 2):
                            for i in roll:
                                if (i == 2):
                                    keepers.append(i)
                                    total += i
                                    onTable -= 1
                            #print("These are the dice I've kept: ",keepers)
                            #sleep(1)
                            #print("This is my score at the moment: ", total)
                            #sleep(1)
                            keepRunning2 = False
                        elif (collect == 3):
                            for i in roll:
                                if (i == 3):
                                    keepers.append(i)
                                    total += i
                                    onTable -= 1
                            #print("These are the dice I've kept: ",keepers)
                            #sleep(1)
                            #print("This is my score at the moment: ", total)
                            #sleep(1)
                            keepRunning2 = False
                        elif (collect == 4):
                            for i in roll:
                                if (i == 4):
                                    keepers.append(i)
                                    total += i
                                    onTable -= 1
                            #print("These are the dice I've kept: ",keepers)
                            #sleep(1)
                            #print("This is my score at the moment: ", total)
                            #sleep(1)
                            keepRunning2 = False
                        elif (collect == 5):
                            for i in roll:
                                if (i == 5):
                                    keepers.append(i)
                                    total += i
                                    onTable -= 1
                            #print("These are the dice I've kept: ",keepers)
                            #sleep(1)
                            #print("This is my score at the moment: ", total)
                            #sleep(1)
                            keepRunning2 = False
                        else:
                            print("Please enter a valid number.")
        else:
            if ('Worm' in keepers and total in dominoes):
                #sleep(1)
                #print(total," points is my score for the round!")
                #sleep(1)
                #beast0319 = addBeastlyScore(beast0319, total, highestDominoe)
                dominoes.remove(total)
                beast0319.append(total)
                keepRunning = False
            else:
                total = 0
                #print("I could not cash out because I did not have a worm.")
                #sleep(1)
                #print("I will receive 0 points.")
                dominoes.pop()
                if (len(beast0319) != 0):
                    dominoes.append(beast0319.pop())
                    dominoes.sort()
                else:
                    dominoes.sort()
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
def collectionAlg(rolled, kept, rounds, opposition, total, dominoes):
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
        weights = {"worms":worms*(2.5),
               "ones":ones*(.5),
               "twos":twos*(.6),
               "threes":threes*(.8),
               "fours":fours*(1.1),
               "fives":fives*(1.4)}
    elif (rounds == 2):
        weights = {"worms":worms*(12),
               "ones":ones*(.7),
               "twos":twos*(.8),
               "threes":threes*(.9),
               "fours":fours*(1.1),
               "fives":fives*(1.3)}
    elif (rounds == 3):
        weights = {"worms":worms*(2.5),
               "ones":ones*(.72),
               "twos":twos*(.87),
               "threes":threes*(1),
               "fours":fours*(1.19),
               "fives":fives*(1.35)}
    elif (rounds == 4):
        weights = {"worms":worms*(2.85),
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

    #Stealing opponents top dominoe
    if (len(opposition) != 0):
        for i in rolled:
            if (i != 'Worm'):
                i = int(i)
                if (i == 1):
                    if (total + 1*ones == opposition[-1]):
                        return int(1)
                elif (i == 2):
                    if (total + 2*twos == opposition[-1]):
                        return int(2)
                elif (i == 3):
                    if (total + 3*threes == opposition[-1]):
                        return int(3)
                elif (i == 4):
                    if (total + 4*fours == opposition[-1]):
                        return int(4)
                elif (i == 5):
                    if (total + 5*fives == opposition[-1]):
                        return int(5)
            elif (i == 'Worm'):
                if (total + 5*worms == opposition[-1]):
                    return 'Worm'

    """
    if (len(dominoes) == 1):
        for i in rolled:
            if (i != 'Worm'):
                i = int(i)
                if (i == 1):
                    if (total + 1*ones == dominoes[-1]):
                        return int(1)
                elif (i == 2):
                    if (total + 2*twos == dominoes[-1]):
                        return int(2)
                elif (i == 3):
                    if (total + 3*threes == dominoes[-1]):
                        return int(3)
                elif (i == 4):
                    if (total + 4*fours == dominoes[-1]):
                        return int(4)
                elif (i == 5):
                    if (total + 5*fives == dominoes[-1]):
                        return int(5)
            elif (i == 'Worm'):
                if (total + 5*worms == dominoes[-1]):
                    return 'Worm'
    """

    #This is for the late game situations
    if (len(dominoes) <= 6):
        for j in reversed(range(len(dominoes))):
            for i in rolled:
                if (i != 'Worm'):
                    i = int(i)
                    if (i == 1):
                        if (total + 1*ones == dominoes[j]):
                            return int(1)
                    elif (i == 2):
                        if (total + 2*twos == dominoes[j]):
                            return int(2)
                    elif (i == 3):
                        if (total + 3*threes == dominoes[j]):
                            return int(3)
                    elif (i == 4):
                        if (total + 4*fours == dominoes[j]):
                            return int(4)
                    elif (i == 5):
                        if (total + 5*fives == dominoes[j]):
                            return int(5)
                elif (i == 'Worm'):
                    if (total + 5*worms == dominoes[j]):
                        return 'Worm'
                
    
    
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
def yesOrNoAlg(kept, total, beast0319, opposition, highestDominoe, dominoes):
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

    highestDominoe = 36
    if (len(dominoes) != 0):
        highestDomino = dominoes[-1]

    
    # Right here is where we start making decisions
    # if something goes wrong check to see if four of a repeat and the 3choose2 possibility is right
    if (worms == 0):
        return True
    if (len(dominoes) <= 6):
        if (total in dominoes):
            return False
    if (len(opposition) != 0):
        if (int(total) == int(opposition[-1])):
            opposition.pop()
            return False
    if ((total in beast0319) or (total not in dominoes)):
        return True
    if (total < 21):
        return True
    elif (repeats <= 3 and slotsRemaining >= 2 and total <= 28): 
        return True
    elif (repeats == 4 and slotsRemaining == 1 and ((threes == 0 and fours == 0) or (threes == 0 and fives == 0) or (fours == 0 and fives == 0))):
        return False
    elif (repeats == 4 and slotsRemaining >= 2  and (fives == 0 and fours == 0)):
        return True
    elif (repeats == 5 and slotsRemaining == 2 and (fives == 0 or fours == 0)):
        return True
    elif (repeats == 5 and slotsRemaining >= 3):
        return True
    else:
        return False


def addBeastlyScore(beast0319, score, highestDominoe):
    if (score >= 21 and score <= highestDominoe):
        beast0319.append(score)
    return beast0319

def removeOpp(opposition, score):
    if (int(score) in opposition):
        opposition.remove(int(score))
    return opposition

def reportWinner(beast0319, opposition):
    worms = {21:1, 22:1, 23:1, 24:1,
             25:2, 26:2, 27:2, 28:2,
             29:3, 30:3, 31:3, 32:3,
             33:4, 34:4, 35:4, 36:4}
    player1Total = 0
    player2Total = 0
    if (len(beast0319) != 0):
        for i in beast0319:
            player1Total += worms[i]
    if (len(opposition) != 0):
        for i in opposition:
            player2Total += worms[i]

    if (player1Total == player2Total):
        return "Draw"
    elif (player1Total > player2Total):
        return "Beast0319"
    else:
        return "Opposition"

             
playerOneWins = 0
playerTwoWins = 0
Draws = 0


while True:
    beastLength = len(beast0319)
    oppLargest = 0
    if (len(dominoes) == 0):
        truth = reportWinner(beast0319, opposition)
        if (truth == "Draw"):
            Draws += 1
        elif (truth == "Beast0319"):
            playerOneWins += 1
        elif (truth == "Opposition"):
            playerTwoWins += 1
        break
    if (len(dominoes) > 0):
        highestDominoe = dominoes[-1]
    #sleep(.75)
    pickomino(beast0319, highestDominoe, dominoes, opposition)
    if (len(dominoes) == 0):
        truth = reportWinner(beast0319, opposition)
        if (truth == "Draw"):
            Draws += 1
        elif (truth == "Beast0319"):
            playerOneWins += 1
        elif (truth == "Opposition"):
            playerTwoWins += 1
        break
    #sleep(.75)
    pickomino(opposition, highestDominoe, dominoes, beast0319)
    _round+=1

print("Player One Wins:",playerOneWins)
print("Player Two Wins:",playerTwoWins)
print("Draws:",Draws)
