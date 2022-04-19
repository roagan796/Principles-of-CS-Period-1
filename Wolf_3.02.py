#Asks for the user's name
inputName = input("Who\'s birthday is it?\t")

def birthday_song(usedName):
  #Prints out the song using the name
  song = f"Happy birthday to you!\nHappy birthday to you!\nHappy birthday dear {usedName}!\nHappy birthday to you!"
  print(song)

#Uses the inputted name from the beginning
birthday_song(inputName)