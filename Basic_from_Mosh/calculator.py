operator = input("Enter an operator (+ - * /) :")

num1 = float(input("Enter you 1st number :"))
num2 = float(input("Enter you 2nd number :"))

if operator == '+' :
  print(num1+num2)
elif operator == '-' :
  print(num1-num2)
elif operator == '*' :
  print(num1*num2)
elif operator == '/' :
  print(num1/num2) 
else : 
  print("Invalid operator")


