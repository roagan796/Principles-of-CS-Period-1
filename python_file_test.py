import random

def mystery_function(x, y):
  random_number = random.randint(0,1)
  if random_number > 0:
    z = x + y
  else:
    z = x * y
  return z
  
result = mystery_function(0, 1)
print(result)

response = input("Non-function method: What temperature F is it today? ")
fahrenheit = int(response)
celsius = 5/9 * (fahrenheit - 32)
celsius = round(celsius, 1)
print(f"{fahrenheit}F is {celsius}C")

def fahrenheitToCelsius(fTemp):
  cTemp = 5/9 * (fTemp - 32)
  return f"{fTemp}F is {round(cTemp, 1)}C"
response = int(input("Function method: What temperature F is it today? "))
print(fahrenheitToCelsius(response))
