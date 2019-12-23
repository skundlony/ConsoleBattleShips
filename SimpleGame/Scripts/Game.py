from Scripts.Player import Player
from Scripts.Codes import StatusCodes

import sys
import random

def shipToPlace(i: int):

    if i > len(player.ships):
        print("Bad ship. Take one from range 1-4")
        return StatusCodes.ERROR

    if player.ships[i-1][1] == 0:
        print("You have used all of this grade ships. Select another")
        return StatusCodes.ERROR

    player.PrintSelfMatrix()
    x = int(input("x?"))
    y = int(input("y?"))

    if player.PlaceOwnShip(i, x, y) == StatusCodes.ERROR:
        Place()

    player.PrintSelfMatrix()

def PrintInfo():
    counter = len(player.ships)
    print("You have: ")
    for i in range(counter):
        j = i+1
        if player.ships[i][1] > 0:
            print(str(j)+") "+str(player.ships[i][0]) +"pool ship.")

def Place():
    try:
        ship = int(input("What ship do u want to place?"))
        shipToPlace(ship)
    except:
        print("You have to use numbers.")
        Place()


def StartBattle():
    return 1


def PrintGreetings():
    print("Welcome to battleships game!")
    print("Please place your ships")


#inits
player = Player()
enemy = Player()



#main game loop
PrintGreetings()
while player.LifePoints > 0 | enemy.LifePoints > 0:
    while player.GetSumOfLeftPools() > 0:
        PrintInfo()
        Place()

    print("Enemy is placing ships.")
    # run method to place enemy ships

    StartBattle()