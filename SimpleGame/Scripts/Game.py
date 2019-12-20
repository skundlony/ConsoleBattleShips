from Scripts.Player import Player
from Scripts.Codes import StatusCodes

import sys
import random

def shipToPlace(i: int):

    if i > 4:
        print("Bad ship. Take one from range 1-4")
        return StatusCodes.ERROR;

    self.PrintSelfMatrix()
    x = int(input("x?"))
    y = int(input("y?"))
    self.PlaceOwnShip(i, x, y)
    self.PrintSelfMatrix()

def PrintInfo():
    counter = len(self.ships)
    print("You have: ")
    for i in range(counter):
        j = i+1
        print(str(j)+"x "+ str(self.ships[i][0]) +"pool ship")

self = Player()
enemy = Player()

print("Welcome to battleships game!")
print("Please place your ships")
PrintInfo()
ship = int(input("What ship do u want to place?"))
shipToPlace(ship)



