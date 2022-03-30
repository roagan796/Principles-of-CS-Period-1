#Used for clear function
import replit

#Welcomes user and explains the story and setting.
print("Welcome pirate! You have sailed all this way towards The Island of Scurvy. Here lies a dungeon where the captain stores away his gold, hidden from all. Many have failed trying to breach his dungeon, but I have faith in you. Get through the captain\'s dungeon and get his gold!")

#These are all the rooms the player can go to.
rooms = [0,1,2,3,4,5]

#This is the variable for the while loop that runs the askUser function.
gameActive = "true"

#These are all used to determine what will be available in each of their rooms
pirateFloor1Room1Alive = "true"
pirateFloor2Room0Alive = "true"
skeletonFloor3Room4Alive = "true"
floor2to3StairsUnlocked = "false"
bossAlive = "true"

#These are all item related variables. The items list serves as the player's inventory.
itemsList = []
swordEquipped = "false"
spiderEquipped = "false"
pillEquipped = "false"
pillRemoved = "false"

#These keep track of the player's current location
currentRoom = rooms[0]
currentFloor = 1

#The user decision variable is changed for every question asked in the program. playAgain is used when the player dies or completes the game and when its true, it will restart the game. The givenPill is used to keep track of when the player gives the old pirate his pill. bossRoomOpen, when true, allows the player to enter Floor 3 Room 0.
userDecision = "none"
playAgain = "false"
bossRoomOpen = "false"
givenPill = "false"

#Used for when the player agrees to playing the game again. It will reset all the variables to default and set them to the very beginning of the game.
def restartGame():
  global currentRoom
  global currentFloor
  global userDecision
  global itemsList
  global swordEquipped
  global pirateFloor1Room1Alive
  global playAgain
  global bossRoomOpen
  global skeletonFloor3Room4Alive
  global bossAlive
  global spiderEquipped
  global pillEquipped
  global pillRemoved
  global givenPill
  global pirateFloor2Room0Alive
  global gameActive

  currentFloor = 1
  currentRoom = 0
  userDecision = "none"
  playAgain = "false"
  swordEquipped = "false"
  itemsList = []
  pirateFloor1Room1Alive = "true"
  pirateFloor2Room0Alive = "true"
  skeletonFloor3Room4Alive = "true"
  bossRoomOpen = "false"
  bossAlive = "true"
  spiderEquipped = "false"
  pillEquipped = "false"
  givenPill = "false"
  gameActive = "true"
  
#The main function that asks all the questions and determines which ones to ask.
def askUser():
  global currentRoom
  global currentFloor
  global userDecision
  global itemsList
  global swordEquipped
  global pirateFloor1Room1Alive
  global pirateFloor2Room0Alive
  global skeletonFloor3Room4Alive
  global bossAlive
  global playAgain
  global bossRoomOpen
  global spiderEquipped
  global pillEquipped
  global pillRemoved
  global givenPill
  global floor2to3StairsUnlocked
  global gameActive
  
  if currentFloor == 1:
    #Floor 1 Room 0
    if currentRoom == 0:
      userDecision = input("\nYou have entered into the first  room of the first floor. There is a door to the EAST  and to the SOUTH.\nWhat do you do?\t")
      if userDecision.lower() == "east":
        currentFloor = 1
        currentRoom = 1
      elif userDecision.lower() == "south":
        currentFloor = 1
        currentRoom = 3
    #Floor 1 Room 1
    elif currentRoom == 1:
      if pirateFloor1Room1Alive == "true":
        if swordEquipped == "false":
          userDecision = input("\nYou have entered into the second room of the first floor. There is a pirate and he GRABs his sword! You can FIGHT him.\nWhat do you do?\t")
          if userDecision.lower() == "grab":
            swordEquipped = "true"
            itemsList.append("Pirate Sword")
            currentFloor = 1
            currentRoom = 1
          elif userDecision.lower() == "fight":
            playAgain = input("\nYou hit him with your fist and it does...nothing. The pirate laughs and cuts you in half. Want to play again? (Y/N) " )
            if playAgain.lower() == "y":
              restartGame()
            else:
              gameActive = "false"
              quit()
        else:
          userDecision = input("\nYou have entered into the second room of the first floor. There is a pirate, but you have his sword! You can FIGHT him.\nWhat do you do?\t")
          if userDecision.lower() == "grab":
            swordEquipped = "true"
            currentFloor = 1
            currentRoom = 1
          elif userDecision.lower() == "fight":
            pirateFloor1Room1Alive = "false"
            currentFloor = 1
            currentRoom = 1
            print("\nYou kill the pirate with his own sword!") 
      else:
        userDecision = input("\nYou have entered into the second room of the first floor. There is a defeated pirate on the ground. There is a room to the EAST and SOUTH. \nWhat do you do?\t")
        if userDecision.lower() == "east":
          currentFloor = 1
          currentRoom = 2
        elif userDecision.lower() == "south":
          currentFloor = 1
          currentRoom = 4
        elif userDecision.lower() == "fight":
          print("\nHe\'s already dead.")
          currentFloor = 1
          currentRoom = 1
    #Floor 1 Room 2
    elif currentRoom == 2:
      userDecision = input("\nYou have entered into the third room of the first floor. There is a stairway leading UP and a room to the WEST. \nWhat do you do?\t")
      if userDecision.lower() == "west":
        currentFloor = 1
        currentRoom = 1
      if userDecision.lower() == "up":
        currentFloor = 2
        currentRoom = 2
    #Floor 1 Room 3
    elif currentRoom == 3:
      userDecision = input("\nYou have entered into the fourth room of the first floor. There is a chest that seems like it can be OPENed! There is also a room to the NORTH. What do you do?\t")
      if userDecision.lower() == "open":
        playAgain = input("\nYou open the chest but it reveals a monster inside that eats you! Play again? (Y/N) " )
        if playAgain== "y":
            restartGame()
    #Floor 1 Room 4
    elif currentRoom == 4:
      userDecision = input("\nYou enter into the fifth room of the first floor. \nThere is a room to the NORTH and to the EAST. What do you do?\t")
      if userDecision.lower() == "north":
        currentFloor = 1
        currentRoom = 1
      elif userDecision.lower() == "east":
        currentFloor = 1
        currentRoom = 5
    #Floor 1 Room 5
    else:
      userDecision = input("\nYou enter into the sixth room of the first floor. \nYou find a CHAIR with a whoopie cushion on it. There is also a room to the WEST. What do you do?\t")
      if userDecision.lower() == "west":
        currentFloor = 1
        currentRoom = 4
      elif userDecision.lower() == "chair":
        print("\nThinking you were funny, it didn\'t do anything.")
  elif currentFloor == 2:
    #Floor 2 Room 0
    if currentRoom == 0:
      if pirateFloor2Room0Alive == "true":
        userDecision = input("\nYou enter into the first room of the second floor. There is a pirate in front of you that you must FIGHT! \nWhat do you do?\t")
        if userDecision.lower() == "fight":
          if len(itemsList) >= 2:
            print("You knock him over with your item in hand and strike him! He falls over and dies.")
            pirateFloor2Room0Alive = "false"
          else:
            playAgain = input("You try to fight with your fists but the pirate slashes them with his golden sword and kills you. Play again? (Y/N)\t")
            if playAgain.lower() == "y":
              restartGame()
            else:
              gameActive = "false"
              quit()
      else:
        userDecision = input("\nYou enter into the first room of the second floor. There is a dead pirate on the ground. There is also a room to the EAST and SOUTH. \nWhat do you do?\t")
        if userDecision == "east":
          currentFloor = 2
          currentRoom = 1
        elif userDecision == "south":
          currentFloor = 2
          currentRoom = 3
    #Floor 2 Room 1
    elif currentRoom == 1:
      userDecision = input("\nYou enter into the second room of the second floor. There is a room to the EAST and WEST. \nWhat do you do?\t")
      if userDecision == "east":
        currentFloor = 2
        currentRoom = 2
      elif userDecision == "west":
        currentFloor = 2
        currentRoom = 0
    #Floor 2 Room 2
    elif currentRoom == 2:
      userDecision = input("\nYou have entered into the third room of the second floor. There is a room to the WEST and SOUTH. There also appears to be a SPIDERWEB in the corner. \nWhat do you do?\t")
      if userDecision.lower() == "west":
        currentFloor = 2
        currentRoom = 1
      elif userDecision.lower() == "south":
        currentFloor = 2
        currentRoom = 5
      elif userDecision.lower() == "spiderweb":
        if spiderEquipped == "false":
          print("\nYou find a weaponized spider in the web. You stash it in your pocket.")
          itemsList.append("Weaponized Spider")
          spiderEquipped = "true"
        else:
          print("\nThere appears to be nothing.")
    #Floor 2 Room 3
    #This room has an old pirate that needs a pill in order to stop blocking the way. Once he is given it, you can access the stairway.
    elif currentRoom == 3:
      if givenPill == "false":
        userDecision = input("\nYou have entered into the fourth room of the second floor. There is an old pirate asking for his medication. If you have it, GIVE it to him to move upstairs. There is also a room to the NORTH and EAST. What do you do?\t")
        if userDecision == "north":
          currentFloor = 2
          currentRoom = 0
        elif userDecision == "east":
          currentFloor = 2
          currentRoom = 4
        elif userDecision == "give":
          if pillEquipped == "true":
            floor2to3StairsUnlocked = "true"
            print("\nHe thanks you and unblocks the doors to the stairs.")
            pillEquipped = "false"
            givenPill = "true"
            itemsList.remove("Pill")
      else:
        userDecision = input("\nYou have entered into the fourth room of the second floor. There is an old pirate that is asleep. There is also a room to the NORTH, EAST and stairs that go UP. What do you do?\t")
        if userDecision == "north":
          currentFloor = 2
          currentRoom = 0
        elif userDecision == "east":
          currentFloor = 2
          currentRoom = 4
        elif userDecision == "up":
          currentFloor = 3
          currentRoom = 3
    #Floor 2 Room 4
    elif currentRoom == 4:
      userDecision = input("\nYou have entered into the fifth room of the second floor. There is a door to the EAST and WEST. What do you do?\t")
      if userDecision.lower() == "west":
        currentFloor = 2
        currentRoom = 3
      elif userDecision.lower() == "east":
        currentFloor = 2
        currentRoom = 5
    #Floor 2 Room 5
    #This is a room with a pill in it that must be given to the old pirate blocking the stairway up. When grabbed, it adds it to the player's inventory and sets the pillRemoved variable to true.
    else:
      if pillRemoved == "false":
        userDecision = input("\nYou enter into the sixth room of the second floor. There is a table with a pill placed on it. You can GRAB it. There is a room to the NORTH and WEST. What do you do? ")
        if userDecision.lower() == "north":
          currentFloor = 2
          currentRoom = 2
        elif userDecision.lower() == "west":
          currentFloor = 2
          currentRoom = 4
        elif userDecision.lower() == "grab":
          print("\nYou grab the pill.")
          pillEquipped = "true"
          pillRemoved = "true"
          itemsList.append("Pill")
      else:
        userDecision = input("\nYou enter into the sixth room of the second floor. There is an empty table. There is also a room to the NORTH and WEST. What do you do? ")
        if userDecision.lower() == "north":
          currentFloor = 2
          currentRoom = 2
          
        elif userDecision.lower() == "west":
          currentFloor = 2
          currentRoom = 4
  else:
    #Floor 3 Room 0
    if currentRoom == 0:
      if bossAlive == "true":
        userDecision = input("\nYou have reached the final room. There is a giant pirate in front of you waiting to FIGHT! What do you do?\t")
        if userDecision.lower() == "fight":
          print("\nAs you attack him, you realize that he is a piece of cardboard that falls over. Anyway, you have found his gold and now have control of the dungeon!")
          bossAlive = "false"
      else:
        playAgain = input("\nPlay again? (Y/N)\t")
        if playAgain.lower() == "y":
          restartGame()
        else:
          gameActive = "false"
          quit()
    #Floor 3 Room 1
    #This is a transition room that hints that there is something in the sixth room aka Room 5
    elif currentRoom == 1:
      if bossRoomOpen == "false":
        userDecision = input("\nYou have entered into the second room of the third floor. There is a closed door with a trail leading to the sixth room. There is a room to the SOUTH and EAST. What do you do?\t")
      else:
        userDecision = input("\nYou have entered into the second room of the third floor. There is an opened door to the WEST. There is a room to the SOUTH and EAST. What do you do?\t")
        if userDecision.lower() == "west":
          currentRoom = 0
          currentFloor = 3
        elif userDecision.lower() == "east":
          currentRoom = 2
          currentFloor = 3
        elif userDecision.lower() == "south":
          currentRoom = 4
          currentFloor = 3
    #Floor 3 Room 2
    #This rooms, like Room 1, is a transition room that hints at the lever and there being something big ahead.
    elif currentRoom == 2:
      userDecision = input("\nYou have entered into the third room of the second floor. Not much in here but a trail to the sixth room and an eerie feeling. There is a room to the WEST and SOUTH. What do you do?\t")
      if userDecision == "west":
        currentFloor = 3
        currentRoom = 1
      elif userDecision == "south":
        currentFloor = 3
        currentRoom = 6
    #Floor 3 Room 3
    elif currentRoom == 3:
      userDecision = input("\nYou have entered into the fourth room of the third floor. There is a stairway leading DOWN and a room EAST. What do you do?\t")
      if userDecision == "east":
        currentFloor = 3
        currentRoom = 4
      elif userDecision == "down":
        currentFloor = 2
        currentRoom = 3
    #Floor 3 Room 4
    #Room has a skeleton inside that can be fought when it is alive. It can be defeated with either the spider or the sword. After that, the player can move on.
    elif currentRoom == 4:
      if skeletonFloor3Room4Alive == "true":
        userDecision = input("\nYou have entered into the fifth room of the third floor and there is a skeleton circling you! You can FIGHT it. What do you do? ")
        if userDecision.lower() == "fight":
          if swordEquipped == "true" or spiderEquipped == "true":
            print("\nYou kill the skeleton with your weapon! You can now move.")
            skeletonFloor3Room4Alive = "false"
          else: 
            playAgain = input("\nYou hit him with your fist and it does...nothing. The skeleton jumps on you and turns you into a skeleton! Play again? (Y/N) " )
            if playAgain.lower() == "y":
              restartGame()
            else:
              gameActive = "false"
              quit()
      else:
        userDecision = input("\nYou have entered into the fifth room of the third floor and there is a skeleton shattered in pieces. There is a room to the NORTH, WEST, and EAST. What do you do?\t")
        if userDecision.lower() == "west":
          currentFloor = 3
          currentRoom = 3
        elif userDecision.lower() == "east":
          currentFloor = 3
          currentRoom = 5
        elif userDecision.lower() == "north":
          currentFloor = 3
          currentRoom = 1
    #Floor 3 Room 5
    #Room has a lever inside that when used, opens the door to the final room which is Floor 3 Room 0.
    else:
      userDecision = input("\nYou have entered into the sixth room of the third floor. There is a room to the NORTH and to the WEST. There is also a LEVER on the ground.\nWhat do you do?\t")
      if userDecision.lower() == "lever":
        if bossRoomOpen == "false":
          bossRoomOpen = "true"
          print("\nYou flick the lever and it locks in. You hear a grinding sound come from the first room of the third floor.")
        else:
          print("\nThe lever has already been switched.")
      elif userDecision.lower() == "north":
        currentFloor = 3
        currentRoom = 2
      elif userDecision.lower() == "west":
        currentFloor = 3
        currentRoom = 4
        
#This loop will repeat the function until the user stops playing
while gameActive == "true":
  askUser()