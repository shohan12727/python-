count = 0 

for number in range(1,101):
  if number %2 != 0 :
    count += 1
    print(number)

print(f"We have {count} odd number")