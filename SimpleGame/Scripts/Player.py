from Scripts.State import State
from Scripts.Codes import StatusCodes

class Player(object):

    # index +1 means how many "pools has one ship" [how many ships left, how many pools of this ships left]
    ships = [[4, 4],
             [3, 6],
             [2, 6],
             [1, 4]]

    LifePoints = 20

    selfMatrix = [[ State.EMPTY for i in range(10)] for j in range (10)]
    enemyMatrix = [[ State.EMPTY for i in range(10)] for j in range (10)]

    # i - HowManyPoolsHasShip, x - cord_X, y - cord_Y
    def PlaceOwnShip(self, i: int, x: int, y: int):
        if self.ships[i][0] == 0:
            print("There is no ship of this type")
            return StatusCodes.ERROR
        
        # how many pools has ship, that how many times places pool.
        # place first pool
        
        howManyPoolsForShip = self.ships[i][1] / self.ships[i][0]

        self.PlaceOnMatrix(x, y)

        #we placed first, but our index in ships is -1 already.
        HowManyPoolsLeft = i

        while HowManyPoolsLeft > 0:
            cord_X = int(input("Next cord X of point?"))
            cord_Y = int(input("Next cord Y of point?"))

            if self.PlaceOnMatrix(cord_X, cord_Y) == 1:
                print("Bad point")
                continue
            # should add method to check if postion is good
            HowManyPoolsLeft -= 1

        return StatusCodes.OK



    def PlaceOnMatrix(self, x: int, y: int):
        if self.selfMatrix[x-1][y-1] == State.EMPTY:
            self.selfMatrix[x-1][y-1] = State.ALIVE
        else: 
            return 1

    # 0 - hit counted, 1 - hit to repeat
    def Hit(self, x: int, y: int):
        if self.enemyMatrix[x][y] == State.EMPTY:
            print("Miss.")
            self.enemyMatrix[x][y] = State.MISS
        elif self.enemyMatrix[x][y] == State.ALIVE:
            print("Hit!")
            self.enemyMatrix[x][y] = State.HIT
        elif self.enemyMatrix[x][y] == State.MISS:
            print("You are trying to repeat hit. Please choose other field")
            return 1
        return 0

    def Defense(self, x: int, y: int):
        if self.enemyMatrix[x][y] == State.ALIVE:
            self.enemyMatrix[x][y] = State.HIT
        return 0

    def PrintSelfMatrix(self):
        print("")
        for i in range(10):
            for j in range(10):
                if self.selfMatrix[i][j] == State.EMPTY:
                    print("[ ]", end = "")
                elif self.selfMatrix[i][j] == State.ALIVE:
                    print("[O]", end = "")
            print("")
        print("")
        return 0





