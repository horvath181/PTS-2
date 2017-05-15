# import for generating random numbers, time delay, object copy
from random import randint
import time
import copy


# create beginning state of game
currentState=((-1, -1, -1, -1, 0), (-1, -1, -1, -1, 0), (-1, -1, -1, -1, 0), (-1, -1, -1, -1, 0))
tmp=[]


# copies state from tuple returns it as a list
def copyState(state):
    return [list(copy.copy(state[0])), list(copy.copy(state[1])),
            list(copy.copy(state[2])), list(copy.copy(state[3]))]


# reloads changed state as tuple from list
def reloadState(state):
    return (tuple(state[0]), tuple(state[1]), tuple(state[2]), tuple(state[3]))


# checks if loaded value is of type int
def load(moving):
    com = -1
    helpCom = input("Your choice: ")
    while True:
        try:
            com = int(helpCom)
            while not com in moving:
                if com > 3:
                    helpCom = input("You don't have figure with that number, try again: ")
                    com = int(helpCom)
                else:
                    helpCom = input("Can't move that one, try again: ")
                    com = int(helpCom)
            return com
                    
        except ValueError:
            helpCom = input("Not a valid value, try again:")
            
    return com


# writes out current state of game
def writeState():
    print("__________________________________________________")
    print("Position \'-1\' means, that the figure is on a starting position.")
    print  ("Player||Figure: Position           ||Score")
    for i in range(0, 4):
        print("% 6d||0:% 4d|1:% 4d|2:% 4d|3:% 4d||% 3d" %
            (i, currentState[i][0], currentState[i][1],
            currentState[i][2], currentState[i][3], currentState[i][4]))
    print("__________________________________________________")


# returns a random number from interval <0,6>
def roll():
    return randint(1,6)


# checks score of players, if someone has 5 points returns True
def checkScore():
    for i in range(0, 4):
        if currentState[i][4] >= 5:
            return [True, i]
    return False


# checks if all players figures didn't move from starting position
def checkPosition(player):
    for i in range(0, 4):
        if tmp[player][i] > -1:
            return False
    return True


# checks if there was any figure owned by another player and moves them to starting position
def checkColisions(player, position):
    for i in range(0, 4):
        if i==player:
            continue
        else:
            for j in range(0, 4):
                if tmp[i][j] == position:
                    tmp[i][j] = -1
                    print("You kicked figure %d of Player %d." % (j, i))
                    time.sleep(1)


# moves player's figure by rolled
def move(player, figure, rolled):
    was = tmp[player][figure]
    finish = player*10
    if was == -1:
        if rolled == 6:
            now = finish
        else:
            print("Unexpected movement.")
            quit()
    else:
        now = tmp[player][figure] + rolled
        if player < 2:
            if was > 10: was -= 40
            now %= 40
        if was in range(finish - 12, finish) and now in range(finish, finish + 12):
            tmp[player][4] += 1
        now %= 40
    
    tmp[player][figure] = now
    print("Moved figure %d to position %d." % (figure, now))
    checkColisions(player, now)


# makes a list of movable figures and returns them as list
def movable(player, rolled, start = False):
    figures=[]
    for i in range(0, 4):
        if start and tmp[player][i] == -1:
                figures.append(i)
        else:
            if tmp[player][i] > -1 or rolled == 6:
                figures.append(i)
    return figures


def main():
    global tmp
    global currentState
    start = time.time()
    # number of current player
    playing = 0
    while checkScore() == False:
        writeState()
        # players round has ended
        ended = False
        print("Player %d's turn." % (playing))
        time.sleep(0.5)
        # counts three throws player has if no figure is in play
        counter = 0
        # automated test
        #com = 0
        tmp = copyState(currentState)
        while checkPosition(playing):
            dice = roll()
            print("Dice: %d" % (dice))
            time.sleep(0.5)
            if dice < 6:
                if counter == 2:
                    print("You couldn't move from starting position, your round ends.")
                    ended = True
                    break
                else:
                    print("You can't move.")
                    time.sleep(1)
            else:
                moving = movable(playing, dice, True)
                print("Possible movements with figures: %s." % (moving))
                com = load(moving)
                move(playing, com, dice)
            counter += 1
        # counts if player rolled 6, if he did he only gets one more roll
        while ended == False and counter < 4:
            dice = roll()
            if dice == 6 and counter == 0:
                counter = 1
            else:
                counter = 4
            print("Dice: ", dice)
            time.sleep(0.5)
            moving = movable(playing, dice)
            print("Possible movements with figures: %s." % (moving))
            com = load(moving)
            if com == -1:
                print("ERROR: Com has not been properly loaded.")
                quit()
            move(playing, com, dice)
        playing = (playing + 1) % 4
        currentState = reloadState(tmp)
        time.sleep(2)
    writeState()
    print("The winner is: Player %d." % (checkScore()[1]))
    print("Program worked", time.time() - start, "seconds")

main()
