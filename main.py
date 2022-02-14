class ConnectFour:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        # table[Y][X]
        self.table = [[0 for _ in range(self.x)] for _ in range(self.y)]

    def dropPiece(self, x: int, team: int) -> int:
        for y in range(self.y):
            if self.table[y][x] == 0:
                if self.changePositionValue(y=y, x=x, value=team):
                    return 2
                return 1
        return 0

    def changePositionValue(self, y: int, x: int, value: int) -> bool:
        # if value <= 3 & rows < self.rows & cols < self.cols:
        self.table[y][x] = value

        return self.checkForWinVertically(y=y, x=x, team=value) \
                or self.checkForWinHorizontally(y=y, x=x, team=value) \
                or self.checkForWinDiagonally(y=y, x=x, team=value)

    def checkForWinVertically(self, y, x, team) -> bool:
        neighbouringCount = 0
        for i in range(1, 4):
            theYPos = y - i
            if neighbouringCount < 3 and theYPos < self.y and self.table[theYPos][x].__eq__(team):
                neighbouringCount += 1
            else:
                break
        return True if neighbouringCount == 3 else False

    def checkForWinHorizontally(self, y, x, team) -> bool:
        neighbouringCount = 0

        for i in range(1, 3):
            for io in range(1, 4):
                theXPosition = x + io if i != 1 else x - io
                if neighbouringCount < 3 and 0 <= theXPosition < self.x and neighbouringCount < 3:
                    if self.table[y][theXPosition] == team:
                        neighbouringCount = neighbouringCount + 1
                    else:
                        break
        return True if neighbouringCount == 3 else False

    def checkForWinDiagonally(self, y, x, team) -> bool:
        neighbouringCount = 0
        for i in range(1, 5):
            for io in range(1, 4):
                theYPosition = y + io if i == 1 or i == 2 else y - io
                theXPosition = x + io if i == 1 or i == 3 else x - io
                if neighbouringCount < 3 and 0 <= theXPosition < self.x and 0 <= theYPosition < self.y:
                    if self.table[theYPosition][theXPosition] == team:
                        neighbouringCount = neighbouringCount + 1
                    else:
                        break
        return True if neighbouringCount == 3 else False

    def printWholeBoard(self):
        for i in range(self.y):
            print(self.table[self.y - 1 - i])


def main():
    board = ConnectFour(x=7, y=6)
    board.printWholeBoard()

    for i in range(1, 43):
        player = 2 if i % 2 == 0 else 1
        if i != 1:
            board.printWholeBoard()
        print(f'Please enter the row number player ${player}')
        rowNum = int(input()) - 1
        inputResult = board.dropPiece(x=rowNum, team=player)
        if inputResult == 0:
            while True:
                board.printWholeBoard()
                print(f'Please enter a valid row number player ${player}')
                rowNum = int(input()) - 1
                inputResult = board.dropPiece(x=rowNum, team=player)
                if inputResult != 0:
                    break
        if inputResult == 2:
            board.printWholeBoard()
            print(f'Player ${player} win!')
            break


if __name__ == '__main__':
    main()
