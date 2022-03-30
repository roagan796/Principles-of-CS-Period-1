#The board
boardPositions = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

#Number of turns
turns = 0

#Used for printing out the current board
def printBoard():
  print(boardPositions[0:3])
  print(boardPositions[3:6])
  print(boardPositions[6:9])

#Gets the position for X. If it's a valid number and turns doesn't exceed 9, it will add an x to the spot, prints the board, and adds a turn. Else, it repeats. Learned global from https://thispointer.com/python-how-to-use-global-variables-in-a-function/#:~:text=with%20same%20name%20%3F-,Use%20of%20%E2%80%9Cglobal%E2%80%A0keyword%20to%20modify%20global%20variable%20inside,at%20start%20of%20function%20i.e.
def getX():
  global turns
  if turns <= 9:
    xPos = int(input("Give a position on the board (1-9): "))
    if xPos >= 1 and xPos <= 9 and (boardPositions[xPos - 1] != 'o' and boardPositions[xPos - 1] != 'x'):
      boardPositions[xPos - 1] = 'x'

      printBoard()

      turns += 1
  
    else:
      getX()

#Gets the position for O. If it's a valid number and turns doesn't exceed 9, it will add an o to the spot, prints the board, and adds a turn. Else, it repeats.
def getO():
  global turns
  if turns <= 9:
    oPos = int(input("Give a position on the board (1-9): "))
    if oPos >= 1 and oPos <= 9 and (boardPositions[oPos - 1] != 'o' and boardPositions[oPos - 1] != 'x'):
      boardPositions[oPos - 1] = 'o'

      printBoard()

      turns += 1
    
    else:
      getO()

#While the turns are less than 9, it will ask for each player's input
while turns < 9:
  if turns < 9:
    getX()
  if turns < 9:
    getO()
  
  
