from State import StateEnum

class Player(object):

    # index +1 means how many "pools has one ship" [how many ships left, how many pools of this ships left]
    ships = [[4, 4],
             [3, 6],
             [2, 6],
             [1, 4]]

    selfMatrix = [[ StateEnum.EMPTY for i in range(10)] for j in range (10)]
    enemyMatrix = [[ StateEnum.EMPTY for i in range(10)] for j in range (10)]

    def PlaceOwnShip(self, i: int, x: int, y: int):
        return 0

    # 0 - hit counted, 1 - hit to repeat
    def Hit(self, x: int, y: int):
        if self.enemyMatrix[x][y] == StateEnum.EMPTY:
            print("Miss.")
            self.enemyMatrix[x][y] == StateEnum.MISS
        elif self.enemyMatrix[x][y] == StateEnum.ALIVE:
            print("Hit!")
            self.enemyMatrix[x][y] == StateEnum.HIT
        elif self.enemyMatrix[x][y] == StateEnum.MISS:
            print("You are trying to repeat hit. Please chose other field")
            return 1
        return 0

    def Defense(self, x: int, y: int):
        if self.enemyMatrix[x][y] == StateEnum.ALIVE:
            self.enemyMatrix[x][y] == StateEnum.HIT
        return 0

    def PrintSelfMatrix(self):
        print("")
        for i in range(0,9):
            for j in range(0,9):
                if self.selfMatrix[i][j] == StateEnum.EMPTY:
                    print("[ ]", end = "")
                elif self.selfMatrix[i][j] == StateEnum.ALIVE:
                    print("[O]", end = "")
            print("")
        print("")
        return 0






