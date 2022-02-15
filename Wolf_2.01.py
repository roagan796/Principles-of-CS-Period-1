print("Welcome to Lab 2.01!\n")

def intMode(): #This is the code for the integer output
  numb = int(input("Enter a number: "))
  print(round((numb) / 2))

def floatMode(): #This is the code for the float output
  numb = float(input("Enter a number: "))
  print((numb) / 2)

mode = input("Integer or float mode? ") #Asks for mode
if mode == "Integer" or "int" or "integer": 
  intMode()
else:
  floatMode()
