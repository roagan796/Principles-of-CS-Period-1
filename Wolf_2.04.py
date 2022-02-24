import time

def prizeTime():
  prizeList = ['a box of cereal.', '$1,000,000.', 'a Lamborghini.', 'a Corvette.', '$1.', 'a vacation to The Bahamas.', 'a PC.', 'a lifetime supply of donuts.', 'an empty box.', 'a mansion.']

  requestedPrize = int(input("Pick a prize between 1-10: "))

  if requestedPrize >= 1 and requestedPrize <= 10:
    print("\nYour prize is " + prizeList[requestedPrize - 1])
  else:
    print("\nInvalid number. Try again.\n")
    time.sleep(2)
    prizeTime() 
prizeTime()

def foodQuiz():
  foodList = ['cheeseburger', 'spaghetti', 'peanut butter and jelly sandwich', 'ice cream', 'chocolate cake', 'pizza']
  
  foodScores = [0,0,0,0,0,0]

  likesCheese = input("\nDo you like cheese? ")
  if likesCheese.lower() == "y":
    foodScores[0] += 1
    foodScores[5] += 1
  
  likesPasta = input("Do you like pasta? ")
  if likesPasta.lower() == "y":
    foodScores[1] += 1
  
  likesDessert = input("Do you like dessert? ")
  if likesDessert.lower() == "y":
    foodScores[3] += 1
    foodScores[4] += 1

  likesMeat = input("Do you like meat? ")
  if likesMeat.lower() == "y":
    foodScores[0] += 1
    foodScores[1] += 1
    foodScores[5] += 1

  likesBread = input("Do you like bread, dough, etc? ")
  if likesBread.lower() == "y":
    foodScores[0] += 1
    foodScores[2] += 1
    foodScores[4] += 1
    foodScores[5] += 1
  
  likesJelly = input("Do you like jelly? ")
  if likesJelly.lower() == "y":
    foodScores[2] += 1

  lacInt = input("Are you lactose intolerant? ")
  if lacInt.lower() == "y":
    foodScores[3] -= 1
    foodScores[4] -= 1

  likesSauce = input("Do you like sauce? ")
  if likesSauce.lower() == "y":
    foodScores[1] += 1
    foodScores[5] += 1
  
  finalFoodList = sorted(zip(foodScores, foodList))

  
  #Prints final results
  
  print(f"\nYour favorite foods are {finalFoodList[-1]} and {finalFoodList[-2]}")
  
foodQuiz()