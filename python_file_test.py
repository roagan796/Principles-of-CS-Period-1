import replit
import time

gameActive = True
playerDecision = "none"

print("Welcome pirate! You have sailed all this way towards The Island of Scurvy. Here lies a dungeon where the captain stores away his gold, hidden from all. Many have failed trying to breach his dungeon, but I have faith in you. Get through the captain\'s dungeon and get his gold!\n")

rooms = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
floors = [1,2,3]

floor1PirateAlive = "true"
floor2PirateAlive = "true"
skeletonAlive = "true"
leverSwitched = "false"

selectedItem = "nothing"
inventorySelectIndex = 10
items = ["sword","pill","weaponized spider"]
inventory = ["nothing"]

currentFloor = 3
currentRoom = 12

f1r0Contents = ["east","south","quit"]
f1r1Contents = ["fight","grab","quit"]
f1r2Contents = ["up","west","quit"]
f1r3Contents = ["north","open","quit"]
f1r4Contents = ["north","east","quit"]
f1r5Contents = ["west","chair","quit"]
f2r0Contents = ["fight","quit"]
f2r1Contents = ["east","west","quit"]
f2r2Contents = ["west","south","down","grab","quit"]
f2r3Contents = ["north","east","give","quit"]
f2r4Contents = ["east","west","quit"]
f2r5Contents = ["grab","west","north","quit"]
f3r0Contents = ["fight","quit"]
f3r1Contents = ["east","south","quit"]
f3r2Contents = ["south","west","quit"]
f3r3Contents = ["down","east","quit"]
f3r4Contents = ["fight","east","west","quit"]
f3r5Contents = ["lever","west","north","quit"]


roomsContents = [f1r0Contents,f1r1Contents,f1r2Contents,f1r3Contents,f1r4Contents,f1r5Contents,f2r0Contents,f2r1Contents,f2r2Contents,f2r3Contents,f2r4Contents,f2r5Contents,f3r0Contents,f3r1Contents,f3r2Contents,f3r3Contents,f3r4Contents,f3r5Contents]

roomDescriptions = ["There is a door to the EAST  and to the SOUTH.","There is a pirate and he GRABs his sword! You can FIGHT him.","There is a stairway leading UP and a room to the WEST.","There is a chest that seems like it can be OPENed! There is also a room to the NORTH.","There is a room to the NORTH and to the EAST.","You find a CHAIR with a whoopie cushion on it.","There is a pirate in front of you that you must FIGHT!","There is a room to the EAST and WEST.","There is a room to the WEST and SOUTH. There also appears to be a spiderweb in the corner that is tempting to GRAB.","There is an old pirate asking for his medication. If you have it, GIVE it to him to move upstairs.","There is a door to the EAST and WEST.","There is a table with a pill placed on it. You can GRAB it. There is a room to the NORTH and WEST.","There is a giant pirate in front of you waiting to FIGHT!","There is a closed door with a trail leading to the sixth room. There is a room to the SOUTH and EAST.","Not much in here but a trail to the sixth room and an eerie feeling. There is a room to the WEST and SOUTH.","There is a stairway leading DOWN and a room EAST.","There is a skeleton circling you! You can FIGHT it.","There is a room to the NORTH and to the WEST. There is also a LEVER on the ground."]

def updateRooms():
  global roomsContents
  global roomDescriptions
  
  roomsContents = [f1r0Contents,f1r1Contents,f1r2Contents,f1r3Contents,f1r4Contents,f1r5Contents,f2r0Contents,f2r1Contents,f2r2Contents,f2r3Contents,f2r4Contents,f2r5Contents,f3r0Contents,f3r1Contents,f3r2Contents,f3r3Contents,f3r4Contents,f3r5Contents]

def restartGame():
  global gameActive
  global playerDecision
  global rooms
  global floors
  global floor1PirateAlive
  global floor2PirateAlive
  global skeletonAlive
  global selectedItem
  global inventorySelectIndex
  global items
  global inventory
  global currentFloor
  global currentRoom
  global f1r1Contents
  global f2r3Contents
  global leverSwitched
  
  gameActive = True
  playerDecision = "none"
  
  rooms = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
  floors = [1,2]
  
  floor1PirateAlive = "true"
  floor2PirateAlive = "true"
  skeletonAlive = "true"
  leverSwitched = "false"
  
  selectedItem = "nothing"
  inventorySelectIndex = 10
  items = ["sword","pill","weaponized spider"]
  inventory = ["nothing"]
  
  currentFloor = 1
  currentRoom = 0

  f1r1Contents = ["fight","grab","quit"]
  f2r3Contents = ["give","north","east","quit"]

while gameActive is True:
  playerDecision = input(f"You are on floor {currentFloor} and in room {currentRoom}. {roomDescriptions[currentRoom]} What do you do? ")
  if playerDecision in roomsContents[currentRoom]:
    if playerDecision.lower() == "east":
      currentRoom += 1
    elif playerDecision.lower() == "west":
      currentRoom -= 1
    elif playerDecision.lower() == "north":
      currentRoom -= 3
    elif playerDecision.lower() == "south":
      currentRoom += 3
    elif playerDecision.lower() == "up":
      currentFloor += 1
      currentRoom += 6
    elif playerDecision.lower() == "down":
      currentFloor -= 1
      currentRoom -=6
    elif playerDecision.lower() == "grab":
      if inventory[0] == "nothing":
        if currentRoom == 1:
          inventory[0] = "sword"
          roomDescriptions[1] = "There is a pirate, but you have his sword! You can FIGHT him."
          f1r1Contents = ["fight"]
          updateRooms()
        elif currentRoom == 8:
          inventory[0] = "weaponized spider"
          f2r2Contents = ["west","south"]
          roomDescriptions[8] = "There is a room to the WEST and SOUTH. There also appears to be an empty spiderweb."
          updateRooms()
        elif currentRoom == 11:
          inventory[0] = "pill"
          f2r5Contents = ["west","north"]
          roomDescriptions[11] = "There is a room to the WEST and NORTH. There also is an empty table."
          updateRooms()
      else:
        if currentRoom == 1:
          inventory.append("sword")
          roomDescriptions[1] = "There is a pirate, but you have his sword! You can FIGHT him if you have it equipped."
          f1r1Contents = ["fight"]
          updateRooms()
        elif currentRoom == 8:
          inventory.append("weaponized spider")
          f2r2Contents = ["west","south"]
          roomDescriptions[8] = "There is a room to the WEST and SOUTH. There also appears to be an empty spiderweb."
          updateRooms()
        elif currentRoom == 11:
          inventory.append("pill")
          f2r5Contents = ["west","north"]
          roomDescriptions[11] = "There is a room to the WEST and NORTH. There also is an empty table."
          updateRooms()
    elif playerDecision.lower() == "fight":
      if currentRoom == 12:
        playerDecision = input("As you attack him, you realize that he is a piece of cardboard that falls over. Anyway, you have found his gold and now have control of the dungeon! Play again?\t")
        replit.clear()
        if playerDecision == "y":
          restartGame()
        else:
          gameActive is False
      elif selectedItem != "sword" and selectedItem != "weaponized spider":
        while playerDecision.lower() != "y" and playerDecision.lower() != "n":
          if currentRoom == 1:
            playerDecision = input("You attack the pirate without a weapon. He laughs and slashes you in half with his sword. Play again?\t")
          elif currentRoom == 6:
            playerDecision = input("You swing at the pirate with your fist but he blocks it. He then attacks and kills you. Play again?\t")
          elif currentRoom == 16:
            playerDecision = input("You try to attack the skeleton without a weapon but miss horribly. It jumps on you and kills you! Play again?\t")
          replit.clear()
        if playerDecision == "y":
          restartGame()
        else:
            gameActive is False
      else:
        if currentRoom == 1:
          floor1PirateAlive = "false"
          f1r1Contents = ["east","south","west","quit"]
          roomDescriptions[1] = "There is a defeated pirate on the ground. There is a room to the EAST, WEST, and SOUTH."
          print("You attack the pirate with a weapon! He falls over in defeat.")
        elif currentRoom == 6:
          floor2PirateAlive = "false"
          f2r0Contents = ["east","south","quit"]
          roomDescriptions[6] = "There is a defeated pirate on the ground. There is a room to the EAST and SOUTH."
          print("You charge at the pirate with your weapon! You crush the pirate!")
        elif currentRoom == 16:
          skeletonAlive = "false"
          f3r4Contents = ["east","north","west","quit"]
          roomDescriptions[16] = "There is a broken skeleton on the ground. There is a room to the EAST, WEST, and NORTH."
          print("You shatter the skeleton with your weapon!")
        updateRooms()
        time.sleep(4)
  
    elif playerDecision == "give":
      if "pill" in inventory:
        if inventory[0] == "pill":
          inventory.remove("pill")
          inventory.append("nothing")
          f2r3Contents = ["north","east","up","quit"]
          roomDescriptions[9] = "There is an old pirate that is asleep. There is also a room to the NORTH, EAST and stairs that go UP."
          updateRooms()
        else:
          inventory.remove("pill")
          f2r3Contents = ["north","east","up","quit"]
          roomDescriptions[9] = "There is an old pirate that is asleep. There is also a room to the NORTH, EAST and stairs that go UP."
          updateRooms()
      else:
        print("You do not have the pill in your inventory.")
        time.sleep(3)
    elif playerDecision == "lever":
      leverSwitched = "true"
      roomsContents[13] = ["west","east","south"]
    elif playerDecision == "chair":
      print("\nThinking you were funny, it didn\'t do anything.")
      time.sleep(4)
    elif playerDecision == "open":
      playerDecision = input("You open the chest but it reveals a monster inside that eats you! Play again? (Y/N)")
      replit.clear()
      if playerDecision == "y":
        restartGame()
      else:
          gameActive is False
  elif playerDecision == "inventory":
    replit.clear()
    print(f"Inventory: {inventory}")
    print(f"Selected item: {selectedItem}")
    while inventorySelectIndex > (len(inventory)) or inventorySelectIndex <= 0 or inventorySelectIndex == "none":
      inventorySelectIndex = int(input("Select an item by its number in the list (1-3): "))
    selectedItem = inventory[inventorySelectIndex - 1]
    inventorySelectIndex = 10
    input("Enter anything to exit out of your inventory. ")
  
  else:
    print(f"{playerDecision} is not a valid input.")
    time.sleep(3)
  replit.clear()