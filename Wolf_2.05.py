boardPositions = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] #These are the positions on the board going from top left to bottom right (zeroth is position 1, eighth is position 9)

#Receives a position on the board. If valid, puts an x on the list in the correct spot then prints out the board. Else, repeats.
def getX():
  xPos = int(input("Give a position on the board (1-9): "))
  if xPos >= 1 and xPos <= 9:
    boardPositions[xPos - 1] = 'x'

    print(boardPositions[0:3])
    print(boardPositions[3:6])
    print(boardPositions[6:9])
  else:
    getX()

getX()