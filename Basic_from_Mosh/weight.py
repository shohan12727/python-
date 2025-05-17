import math

weight = float(input("Enter your weight :"))

unit = input ("Enter pound or weight (K for kilograms, P for pounds) :").upper()

if unit == 'K' :
  weight = weight * 2.20462 
elif unit == 'P':
  weight = weight /  2.20462 
else : 
  print("Invalid input")

print(f"your weight is {round(weight,1)}")      