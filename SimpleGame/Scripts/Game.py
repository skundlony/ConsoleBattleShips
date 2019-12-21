from Scripts.Player import Player
from Scripts.Codes import StatusCodes

import sys
import random

def shipToPlace(i: int):

    if i > len(player.ships):
        print("Bad ship. Take one from range 1-4")
        return StatusCodes.ERROR;

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
        print(str(j)+"x "+ str(player.ships[i][0]) +"pool ship")

def Place():
    ship = int(input("What ship do u want to place?"))
    shipToPlace(ship)

player = Player()
enemy = Player()



print("Welcome to battleships game!")
print("Please place your ships")
while 1:
    PrintInfo()
    Place()


