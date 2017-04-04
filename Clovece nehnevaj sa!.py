# import for generating random numbers, time delay, object copy
import random
import time
import copy

# create beginning state of game
currentState=((-1,-1,-1,-1,0),(-1,-1,-1,-1,0),(-1,-1,-1,-1,0),(-1,-1,-1,-1,0))
tmp=[]

# copies state from tuple returns it as a list
def copyState(state):
    helper=[list(copy.copy(state[0])),list(copy.copy(state[1])), list(copy.copy(state[2])), list(copy.copy(state[3]))]
    return helper

# reloads changed state as tuple from list
def reloadState(state):
    helper=(tuple(state[0]),tuple(state[1]),tuple(state[2]),tuple(state[3]))
    return helper

# writes out current state of game
def writeState():
    print("Position \'-1\' means, that the figure is on a starting position.")
    print("Player||Figures                    ||Score")
    for i in range(0,4):
        print("% 6d||0:% 4d|1:% 4d|2:% 4d|3:% 4d||% 3d"%(i,currentState[i][0],currentState[i][1],currentState[i][2],currentState[i][3],currentState[i][4]))

# returns a random number from interval <0,6>
def roll():
    return random.randint(1,6)

# checks score of players, if someone has 5 points returns True
def checkScore():
    for i in range(0,4):
        if currentState[i][4]>=5:
            return [True,i]
    return False

# checks if all players figures didn't move from starting position
def checkPosition(player):
    for i in range(0,4):
        if tmp[player][i]>-1:
            return False
    return True

# checks if there was any figure owned by another player and moves them to starting position
def checkColisions(player, position):
    for i in range(0,4):
        if i==player:
            continue
        else:
            for j in range(0,4):
                if tmp[i][j]==position:
                    tmp[i][j]=-1
                    print("You kicked figure %d of Player %d."%(j,i))
                    time.sleep(1)

# moves player's figure by rolled
def move(player, figure, rolled):
    was=tmp[player][figure]
    finish=player*10
    now=tmp[player][figure]+rolled
    if player<2:
        was=was-40
    if was in range(finish-12,finish) and now in range(finish,finish+12):
        tmp[player][4]+=1
    tmp[player][figure]=(tmp[player][figure]+rolled)%40
    print("Moved figure %d to %d."%(figure,tmp[player][figure]))
    checkColisions(player, tmp[player][figure])

# makes a list of movable figures an returns them as string
def movable(player, rolled, start=False):
    figures=[]
    for i in range(0,4):
        if start and tmp[player][i]==-1:
                figures.append(i)
        else:
            if tmp[player][i]>-1 or rolled==6:
                figures.append(i)
    return str(figures).strip('[]')

def main():
    global tmp
    global currentState
    # number of current player
    playing=0
    while checkScore()==False:
        writeState()
        # players round has ended
        ended=False
        print("Player %d's turn."%(playing))
        time.sleep(0.5)
        # counts three throws player has if no figure is in play
        counter=0
        tmp=copyState(currentState)
        while checkPosition(playing):
            dice=roll()
            print("Dice: %d"%(dice))
            time.sleep(0.5)
            if dice<6:
                if counter==2:
                    print("You couldn't move from starting position, your round ends.")
                    ended=True
                    break
                else:
                    print("You can't move.")
                    time.sleep(1)
            else:
                moving=movable(playing,dice,True)
                print("Possible movements with figures: %s."%(moving))
                com=int(input("Your choice: "))
                while not com in moving:
                    com=int(input("Can't move that one, try again: "))
                tmp[playing][com]=0+(playing*10)
                print("Moved figure %d to %d."%(com,tmp[playing][com]))
                checkColisions(playing, tmp[playing][com])
            counter+=1
        # counts if player rolled 6, if he did he only gets one more roll
        while ended==False and counter<4:
            dice=roll()
            if dice==6 and counter==0:
                counter=1
            else:
                counter=4
            print("Dice: ",dice)
            time.sleep(0.5)
            moving=movable(playing,dice)
            print("Possible movements with figures: %s."%(moving))
            com=int(input("Your choice: "))
            while not com in moving:
                com=int(input("Can't move that one, try again: "))
            move(playing,com,dice)
        playing=(playing+1)%4
        currentState=reloadState(tmp)
        time.sleep(2)
    writeState()
    print("The winner is: Player %d."%(checkScore()[1]))

main()
