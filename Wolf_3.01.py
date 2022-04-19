import random
import time
import os

#Initial clearing of the console
os.system('clear')

#Game loop starts
gameActive = True

#Gives the user an intro
print("I am the Magic 8-Ball. You will ask me a question and I will give you my response. This is your destiny, not a python function.\n")

#Every response possible for the magic 8-ball
responses = ["It is certain.","It is decidely so.","Without a doubt.","Reply hazy, try again.","Ask again later.","Don\'t count on it.","My reply is no.","My sources say no."]

#Game loop that will ask the user a question, give a random response, and then ask to play again. If they say again but "y", the game loop stops.
while gameActive is True:
  userQuestion = input("What do you ask the magic 8-ball?\t")

  responseIndex = (random.randint(0, 7))

  ballResponse = responses[responseIndex]

  print(f"{ballResponse}")
  time.sleep(4)

  playAgain = input("\nPlay again? (Y/N):\t")

  if playAgain.lower() != "y":
    quit()  
  
  os.system('clear')