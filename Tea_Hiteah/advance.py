import time 

wait_time = 1 
max_retires = 5 
attemps = 0

while attemps < max_retires :
  print("Attemps",attemps, +1,"wait time",wait_time)
  time.sleep(wait_time)
  wait_time *=2 
  attemps += 1