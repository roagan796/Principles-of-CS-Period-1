import random
import time
import os

os.system('clear')

gameActive = True

#Every response possible for the magic 8-ball
responses = ["It is certain.","It is decidely so.","Without a doubt.","Yes definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don\'t count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]

while gameActive is True:
  userQuestion = input("What do you ask the magic 8-ball?\t")

  responseIndex = (random.randint(0, 19))

  ballResponse = responses[responseIndex]

  print(f"{ballResponse}")
  time.sleep(4)

  playAgain = input("Play again? (Y/N):\t")

  if playAgain.lower() != "y":
    quit()  
  
  os.system('clear')