# 1. userName is no more than 12 characters 
# 2. userName must not contain spaces 
# 3. userName must not contain digits 

# user_name = input ("Enter your name : ")

# if user_name.len >= 12 :
#   print("Invalid")
# elif " "  in user_name :
#   print("Invalid")
# elif  any(char.isdigit() for char in user_name)
#   print("Invalid")
# else :
#   print("Valid")  


userName = input("Enter your name ")


if len(userName) > 12 :
  print ("You jerk ! you are not suppossed to be her ")
elif not userName.find(" ") == -1 :
  print("Get out")
elif not  userName.isalpha() :
  print ("Fuck you ")  
#isAlpha mane holo je eita sob gula character kintu amar lagbe holo emon name jekhane 
# character jodi na pay tahole take dhorbe ejonno prothome not lagano.....
# samjhaaa! dayaaaaaaaaaaaaaa!  
else :
  print(f"Welcome {userName}")  

 


























