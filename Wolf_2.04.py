def foodQuiz(): #defines the food quiz function
  foodList = ['cheeseburger', 'spaghetti', 'peanut butter and jelly sandwich', 'ice cream', 'chocolate cake', 'pizza'] #makes the list of foods
  
  foodScores = [0,0,0,0,0,0] #list of scores for each food

  likesCheese = input("\nDo you like cheese? (y / n)\t ") #asks if user likes cheese and if so, adds scores to the respective foods
  if likesCheese.lower() == "y": 
    foodScores[0] += 1 #cheeseburger
    foodScores[5] += 1 #pizza
  
  likesPasta = input("Do you like pasta? (y / n)\t ") #asks if user likes pasta and if so, adds score to the respective food
  if likesPasta.lower() == "y":
    foodScores[1] += 1 #spaghetti
  
  likesDessert = input("Do you like dessert? (y / n)\t ") #asks if user likes dessert and if so, adds a scores to the respective foods
  if likesDessert.lower() == "y":
    foodScores[3] += 1 #ice cream
    foodScores[4] += 1 #chocolate cake

  likesMeat = input("Do you like meat? (y / n)\t ") #asks if user likes meat and if so, adds scores to the respective foods
  if likesMeat.lower() == "y":
    foodScores[0] += 1 #cheeseburger
    foodScores[1] += 1 #spaghetti because of the meatballs
    foodScores[5] += 1 #pizza

  likesBread = input("Do you like bread, dough, etc? (y / n)\t ") #asks if user likes bread and if so, adds scores to the respective foods
  if likesBread.lower() == "y":
    foodScores[0] += 1 #cheeseburger
    foodScores[2] += 1 #pb&j sandwich
    foodScores[4] += 1 #chocolate cake
    foodScores[5] += 1 #pizza because of crust
  
  likesJelly = input("Do you like jelly? (y / n)\t ") #asks if user likes jelly and if so, adds score to the respective food
  if likesJelly.lower() == "y":
    foodScores[2] += 1

  lacInt = input("Are you lactose intolerant? (y / n)\t ") #asks if user is lactose intolerant and if so, removes scores from the respective foods
  if lacInt.lower() == "y":
    foodScores[3] -= 1 #ice cream
    foodScores[4] -= 1 #chocolate cake

  likesSauce = input("Do you like sauce? (y / n)\t ") #asks if user likes sauce and if so, adds scores to the respective foods
  if likesSauce.lower() == "y":
    foodScores[1] += 1 #spaghetti
    foodScores[5] += 1 #pizza
  
  finalFoodList = sorted(zip(foodScores, foodList)) #combines both lists into one, then sorts them

  
  #Prints final results by finding the foods with the highest and second highest scores
  
  print(f"\nYour favorite foods are {finalFoodList[-1]} and {finalFoodList[-2]}")
  
foodQuiz() #runs the program
