#Used for pauses between outputs
import time

#This is all within a function so it can be repeated
#Asks for each side
def triangleQuestion():
  sideX = int(input("What is the length of side x? (Whole number) \t"))
  sideY = int(input("What is the length of side y? (Whole number) \t"))
  sideZ = int(input("What is the length of side z? (Whole number) \t"))
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

#Runs the program
triangleQuestion()