unit = input ("Enter the unit value (F/C) :").upper()
temp = int(input("Enter the curernt temperature : "))

if  unit == "C" :
  Farenhite = (temp*(9/5))+32
  print(f"Now the asmophere is {Farenhite} degree farenhite")
elif unit == "F" :
  celcius = (temp - 32) * (5/9)  
  print(f"Now the atmosphere is {celcius} degree celcius")
else :
  print ("Invalid unit")  