import math 
def circle (radius) :
  area = round(( math.pi * pow (radius,2)),2) 
  circumference = round((2 * math.pi* radius),2) 
  return area, circumference

print(circle(5))
