principal = 0
rate = 0 
time = 0 

while principal <= 0 :
  principal = int(input("Enter the Principal ammount: "))
  if principal <=0 :
    print("Principal can't be less than zero or zero")
    

  
while rate <= 0 :
  rate = float(input("Enter the rate of interest: "))
  if rate <= 0 :
    print("Rate can't be zero and less than zero")
    

while time <= 0 :
  time = int(input("Enter the time in years: ")) 
  if time <=0 :
    print ("Time can't be zero or less than zero") 
    

Totat_Ammount = principal * pow((1+(rate/100)),time)   

print (f"The Total balance of your bank {round(Totat_Ammount,2)}")













