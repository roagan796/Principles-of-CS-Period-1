#President question

print("Can you be president?\n")

#This asks for the user's age, years of residency in the USA, and if they are a naturally born citizen.
age = int(input("How old are you? "))
yearsResident = int(input("How many years have you been a US resident? "))
natBornCitizen = input("Are you a naturally born citizen? ")

#If they are older than 35, been a resident for 14 or more years, and are a naturally born citizen, then they can be the president. Else, they cannot.
if age > 35 and yearsResident >= 14 and natBornCitizen == "yes":
  print("You can be the president!")
else:
  print("Sorry, but you cannot be the president.");

#Roller coaster question

print("\nCan you ride the roller coaster?\n")

#Asks for user height, if they have a frequent rider pass, and the amount of quarters they have. Uses the age from before.
height = int(input("How tall are you in inches? "))
freqRiderPass = input("Do you have a frequent rider pass? ")
quarters = int(input("How many quarters do you have? "))

#This asks if they are more than 50 inches tall or over the age of 18 and they have 4 or more quarters. If so, it will ask if they have a frequent rider pass and if they have 2 or more quarters. If true, then they can ride. Else, they should still be able to ride as they still have 4 quarters. If none of those requirements are met, then they cannot ride.
if height > 50 or age > 18:
  if  freqRiderPass == "yes" and quarters >= 2:
    print("You can ride the roller coaster for 2 quarters!")
  elif freqRiderPass == "no" and quarters >= 4:
    print("You can ride the roller coaster for 4 quarters!")
  else:
    print("Sorry, but you  cannnot ride the roller coaster.")
else:
  print("Sorry, but you  cannnot ride the roller coaster.")