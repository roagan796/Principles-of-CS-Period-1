import os

#Clears screen
os.system('clear')

#Used for game loop
gameActive = True

#All board spots
boardPositions = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

#Every win possibility
win246 = [2,4,6]
win048 = [0,4,8]
win012 = [0,1,2]
win345 = [3,4,5]
win678 = [6,7,8]
win036 = [0,3,6]
win147 = [1,4,7]
win258 = [2,5,8]

#Input variables for X and O
xPos = 0
oPos = 0

#Used to restart game when the game has a winner or a tie and the player chooses to restart
def restartGame():
  global xPos
  global oPos
  global gameActive
  global boardPositions
  global userInputs
  
  xPos = 0
  oPos = 0
  gameActive = True
  boardPositions = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
  userInputs = 0

#Asks if the player wants to play again. Called when the game has a winner or ties.
def playAgainQues():
  global playAgain
  global gameActive
  
  playAgain = input("Want to play again? (Y/N)\t")
  if playAgain.lower() == "y":
    restartGame()
  else:
    gameActive = False
    quit()

#Creates the board
def printBoard():
  print(f"_________________________")
  print(f"|                       |")
  print(f"|                       |")
  print(f"|    {boardPositions[0]}      {boardPositions[1]}      {boardPositions[2]}    |")
  print(f"|                       |")
  print(f"|                       |")
  print(f"|    {boardPositions[3]}      {boardPositions[4]}      {boardPositions[5]}    |")
  print(f"|                       |")
  print(f"|                       |")
  print(f"|    {boardPositions[6]}      {boardPositions[7]}      {boardPositions[8]}    |")
  print(f"|                       |")
  print(f"|_______________________|")
  
  #print(boardPositions[0:3])
  #print(boardPositions[3:6])
  #print(boardPositions[6:9])


#Used to keep track of how many moves have been made
userInputs = 0

while gameActive is True:
  while userInputs <= 9:
    while xPos < 1 or xPos > 9 or boardPositions[xPos - 1] == 'X' or boardPositions[xPos - 1] == "O":
      os.system('clear')
      printBoard()
      xPos = int(input("Give a position on the board, X (1-9): "))
    oPos = 0
    boardPositions[xPos - 1] = 'X'
    #Checks every possible win for X's
    if ([boardPositions[i] for i in (win246)] == ['X','X','X']) or ([boardPositions[i] for i in (win048)] == ['X','X','X']) or ([boardPositions[i] for i in (win012)] == ['X','X','X']) or ([boardPositions[i] for i in (win036)] == ['X','X','X']) or ([boardPositions[i] for i in (win147)] == ['X','X','X']) or ([boardPositions[i] for i in (win345)] == ['X','X','X']) or ([boardPositions[i] for i in (win678)] == ['X','X','X']) or ([boardPositions[i] for i in (win258)] == ['X','X','X']):
      os.system('clear')
      printBoard()
      print('X\'s win!')
      playAgainQues()
    else:
      os.system('clear')
    userInputs += 1
    
    
    while oPos < 1 or oPos > 9 or boardPositions[oPos - 1] == 'X' or boardPositions[oPos - 1] == "O":
      os.system('clear')
      printBoard()
      oPos = int(input("Give a position on the board, O (1-9): "))
    boardPositions[oPos - 1] = 'O'
    xPos = 0
    #Checks every possible win for O's
    if ([boardPositions[i] for i in (win246)] == ['O','O','O']) or ([boardPositions[i] for i in (win048)] == ['O','O','O']) or ([boardPositions[i] for i in (win012)] == ['O','O','O']) or ([boardPositions[i] for i in (win036)] == ['O','O','O']) or ([boardPositions[i] for i in (win147)] == ['O','O','O']) or ([boardPositions[i] for i in (win345)] == ['O','O','O']) or ([boardPositions[i] for i in (win678)] == ['O','O','O']) or ([boardPositions[i] for i in (win258)] == ['O','O','O']):
      os.system('clear')
      printBoard()
      print('O\'s win!')
      playAgainQues()
    else:
      os.system('clear')
    userInputs += 1

  #When there are 9 inputs, the game ties
  printBoard()
  print("A tie!")
  playAgainQues()
  
