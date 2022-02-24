#Used for pauses between outputs
import time

#This is all within a function so it can be repeated
#Asks for each side
def triangleQuestion():
  #Learned this from a Quora question https://www.quora.com/How-do-I-accept-multiple-integers-as-input-on-a-single-line-in-Python
  sidesList = list(map(int, input("Enter each side length: ").split()))

  sideX = sidesList[0]
  sideY = sidesList[1]
  sideZ = sidesList[2]  
  #Determines the type of triangle. If invalid sides, repeats.
  if (sideX + sideY) > sideZ:
    print(f"\nThe perimeter of the triangle is {sideX + sideY + sideZ}.") 
    time.sleep(2)
    if sideX ** 2 + sideY ** 2 == sideZ ** 2:
      print("\nThis is a right triangle!")
      time.sleep(2)
    if sideX == sideY and sideY == sideZ:
      print("\nThis is an equilateral triangle!")
    else:
      if sideZ == sideX or sideZ == sideY or sideX == sideY:
        print("\nThis is an isosceles triangle!")
      else:
        print("\nThis is a scalene triangle!")
  else:
    print("\nSorry, this does not make a triangle. Try again.\n")
    time.sleep(3)
    triangleQuestion()

#Runs the triangle program
triangleQuestion()

#Declares the prizes and the statement before announcing the prize
def gameShow():
  prizeList = ["a Honda Civic.", "a bag of Lays Classic Potato Chips.", "a beach house in the Caribbean.", "a Macbook.", "a Samsung Galaxy.", "a Corvette.", "an autograph of your favorite celebrity.", "tickets to a concert.", "$100,000.","50¢."]

  #Asks for which prize the user wants
  requestedPrize = int(input("\nWhat prize do you want? (1-10) "))

  #Determines if the prize is valid and prints it out if the requested prize is 1-10
  if requestedPrize >= 1 and requestedPrize <= 10:
    print("\nYour prize is " + prizeList[requestedPrize - 1])
  else:
    print("That number isn't valid. Enter a different one.\n")
    time.sleep(3)
    gameShow()

#Runs the game show 
gameShow()

