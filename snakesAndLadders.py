"""Module to simulate snakes and ladders
"""

import random

"""
Creates snakes and ladders game board
board[x] is the square the player will end up on if they land on square[x]
example: they land on board[1] (square 1) they head to square 37 - ladder
returns: list of length 100 representing a set snakes and ladders board
"""
def boardCreate():
    board=list(range(1,101))

    board[1]=37
    board[6]=13
    board[7]=30
    board[14]=25
    board[16]=5
    board[20]=41
    board[35]=43
    board[45]=24
    board[48]=10
    board[50]=66
    board[61]=19
    board[63]=59
    board[70]=90
    board[73]=52
    board[77]=97
    board[86]=93
    board[91]=87
    board[94]=74
    board[99]=79
    return board

"""
provides the advantage headstart simulation
Works by changing list values giving as parameters
Only to be used inside the snakes and ladders function (or to see how many times game is won within advantage rolls)

param board: the snakes and ladders board being played
param players: list of players involved in the game
param advantage: integer giving the headstart for the 1st player
param location: list storing the board location for each player
param ENDSQUARE: the final square where once reached a player wins the game

return: nothing, OR player if a player wins
"""
def snakesAndLaddersAdvantage(board,players,advantage,location,ENDSQUARE):
    for i in range(advantage):
        roll = random.randint(1,6)
        location[0]=location[0]+roll
        if (location[0]>=ENDSQUARE):
            return (players[0])
        location[0]=board[location[0]]


"""
Plays a game of snakes and Ladders until a win with allowing the first player to get a headstart on rolls

param board: the board to play on, in the format of a list of integers, 
        where each integer inside the board represents a position
param playerNumber: the number of players to play the game, integer
param advantage: the headstart in rolls the first player gets, integer, default 0
param maxRolls: maximum number of rolls for each player before a too many rolls exception is thrown, default 10000
return: the player number of the player that wins, player number starts at 1
raises StopIteration
"""
def snakesAndLadders(board,playerNumber,advantage=0, maxRolls=10000):
    ENDSQUARE=len(board)
    players=list(range(1,playerNumber+1))
    location=[0]*playerNumber
    
    #advantage 'headstart' for first player
    if (advantage>0):
        snakesAndLaddersAdvantage(board,players,advantage,location,ENDSQUARE)
        if (location[0]>=ENDSQUARE):
            return players[0]
    rollCount=0
    #game after headstart, or with no headstart
    while (True and rollCount<maxRolls):
        rollCount +=1
        for i in range(0,playerNumber):
            roll=random.randint(1,6)
            #print(players[i], "has rolled", roll)
            location[i]=location[i]+roll
            if (location[i]>=ENDSQUARE):
                #print(players[i], "Has won")
                return (players[i])
            else:
                location[i]=board[location[i]]
            #print(players[i], "is in square", location[i])
    raise StopIteration("Over max rolls")

"""
Runs and prints results of simulation to console

param runSize: the number of times the game is played
param playerNumber: the number of players playing the game
param board: the game board that is played on, has a default game board
param advantage: the number of free rolls the first player gets before others can start rolling

"""
def simulateSnakesAndLadders(runSize, playerNumber, board=boardCreate(),advantage=0):
    result=[0]*playerNumber
    try:
        for i in range(runSize):
            result[(snakesAndLadders(board,playerNumber,advantage))-1]+=1
    except StopIteration:
        print("Went over max rolls, simulation stopped early")

    for i in range(1,playerNumber+1):
        print("player %i: %i" %(i, result[i-1]))

simulateSnakesAndLadders(10000,3)