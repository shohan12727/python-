
# Example 1 : 
i = 0 
while i <= 5 :
  print (i)
  i  += 1 

# Example 2 : 

name = input("Enter your name: ")

while name == '' : 
  print("You did not enter your name ")
  name = input("Enter your name: ")



#example 3 :

num = int(input("Enter a number between 1 to 10 : "))

while num < 1 or num > 10 :
  print (f"{num} is not valid ")
  num = int(input("Enter a number between 1 to 10 : "))

print("Great! you pass valid value.")












