from Scripts.State import State
from Scripts.Codes import StatusCodes

class Player(object):

    # index +1 means how many "pools has one ship" [how many ships left, how many pools of this ships left]
    ships = [[1, 4],
             [2, 6],
             [3, 6],
             [4, 4]]

    #sum of ship pools
    LifePoints = 20

    selfMatrix = [[ State.EMPTY for i in range(10)] for j in range (10)]
    enemyMatrix = [[ State.EMPTY for i in range(10)] for j in range (10)]

    # i - HowManyPoolsHasShip, x - cord_X, y - cord_Y
    def PlaceOwnShip(self, i: int, x: int, y: int):

        x -= 1
        y -= 1

        if self.CheckForShipPlace(i, x, y) == StatusCodes.ERROR:
            return StatusCodes.ERROR

        placedPools = 0

        # players typing shop from 1 to 4
        # matrix indexes are from 0 to 3
        # so we have to decrease value
        i -= 1

        if self.CheckForGoodPostion(x, y, 0, 0) == StatusCodes.ERROR:
            return StatusCodes.ERROR

        self.PlaceOnMatrix(x, y)
        placedPools += 1

        #we placed first, but our index in ships is -1 already.
        HowManyPoolsLeft = i
        straightCord = [0,0]

        while HowManyPoolsLeft > 0:
            
            cord_X = x
            cord_Y = y

            if straightCord != [x, 0]:

                while 1:
                    try:
                        cord_X = int(input("Next cord X of point?"))
                        if(0 < cord_X < 11):
                            cord_X -=1
                            break
                        else:
                            print("Type range 1-10")
                    except:
                        print("Cords are numbers with range 1-10.")

            if straightCord != [0, y]:
                
                while 1:
                    try:
                        cord_Y = int(input("Next cord Y of point?"))
                        if(0 < cord_Y < 11):
                            cord_Y -= 1
                            break
                        else:
                            print("Type range 1-10")
                    except:
                        print("Cords are numbers with range 1-10.")

            if self.CheckForGoodPostion(cord_X, cord_Y, x, y) == StatusCodes.ERROR:
                print("Bad point. Type another.")
                continue

            if x == cord_X:
                straightCord = [x,0]
            elif y == cord_Y:
                straightCord = [0,y]

            self.PlaceOnMatrix(cord_X, cord_Y)
            placedPools += 1
            HowManyPoolsLeft -= 1

            # we have to store last point in x and y vars
            x = cord_X
            y = cord_Y
        
        left = self.ships[i][1]
        self.ships[i] = [i+1 ,left - placedPools]
        return StatusCodes.OK

    #before we placing a ship, we have to check that we have a space to place it
    def CheckForShipPlace(self, i: int, x: int, y: int):

        if self.selfMatrix[x][y] == State.ALIVE:
            return StatusCodes.ERROR

        poolsToCheck = i - 1
        errors = 0
        singleErrors = i - 1
        minRangeX = x-poolsToCheck
        maxRangeX = x+poolsToCheck
        minRangeY = y-poolsToCheck
        maxRangeY = y+poolsToCheck

        if minRangeX > 0:
            minRangeX = 1

        if minRangeY > 0:
            minRangeY = 1

        if maxRangeX > 10:
            maxRangeX = 10

        if maxRangeY > 10:
            maxRangeY = 10

        for rangeX in range(minRangeX, x):
            if self.selfMatrix[rangeX][y] != State.EMPTY:
                errors += 1
                break

        for rangeX in range(x, maxRangeX):
            if self.selfMatrix[rangeX][y] != State.EMPTY:
                errors += 1
                break

        for rangeY in range(minRangeY, y):
            if self.selfMatrix[x][rangeY] != State.EMPTY:
                errors += 1
                break

        for rangeY in range(y, maxRangeY):
            if self.selfMatrix[x][rangeY] != State.EMPTY:
                errors +=1
                break

        if errors == 4:
            return StatusCodes.ERROR

        return StatusCodes.OK



    def CheckForGoodPostion(self, x: int, y: int, lastX: int, lastY: int):

        minRangeX = x-1
        maxRangeX = x+1
        minRangeY = y-1
        maxRangeY = y+1

        if minRangeX > 0:
            minRangeX = 1

        if minRangeY > 0:
            minRangeY = 1

        if maxRangeX > 10:
            maxRangeX = 10

        if maxRangeY > 10:
            maxRangeY = 10

            # logic error
        for rangeX in range(x-1, x+1):
            for rangeY in range(y-1, y+1):
                if self.selfMatrix[rangeX][rangeY] != State.EMPTY:
                    if lastX != 0 & lastY != 0 & rangeX != lastX & rangeY != lastY:
                        return StatusCodes.ERROR
        return StatusCodes.OK

    # Placing single block on matrix
    def PlaceOnMatrix(self, x: int, y: int):
        if self.selfMatrix[x][y] == State.EMPTY:
            self.selfMatrix[x][y] = State.ALIVE
            print("Placed.")


    def Hit(self, x: int, y: int):
        if self.enemyMatrix[x][y] == State.EMPTY:
            print("Miss.")
            self.enemyMatrix[x][y] = State.MISS
        elif self.enemyMatrix[x][y] == State.ALIVE:
            print("Hit!")
            self.enemyMatrix[x][y] = State.HIT
            return State.HIT
        elif self.enemyMatrix[x][y] == State.MISS:
            print("You are trying to repeat hit. Please choose other field.")
            StatusCodes.ERROR
        return StatusCodes.OK


    def Defense(self, x: int, y: int):
        if self.enemyMatrix[x][y] == State.ALIVE:
            self.enemyMatrix[x][y] = State.HIT
        return StatusCodes.OK

    # Prints Matrix
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