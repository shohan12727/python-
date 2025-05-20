Marks = [] 

for mark in range (1,6) :
  value = int(input(f"Display your mark in sub {mark}: "))
  Marks.append(value)

Result = sorted(Marks)

print(f"Your result's list: {Result}")

# for res in Result :
#   print(res)
avarage = sum(Result) / len(Result)

print(f"The avarage of all mark {avarage}")
