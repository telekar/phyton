# For each step, take the previous value, 
# and replace each run of digits (like 111) with the number of digits (3)
# followed by the digit itself (1)
# run xx times - what is the length

import time

time_start = time.perf_counter()


with open ( "puzzle_10a.txt","r") as f:
    inputstr1 = f.read()

inputstr2 = inputstr1

def look_and_say(zahl):

  result = ""
  count = 1
  for i in range(1, len(zahl)):
    if zahl[i] == zahl[i-1]:
      count += 1
    else:
      result += str(count) + zahl[i-1]
      count = 1
  result += str(count) + zahl[-1]
  return result

for _ in range(40):
  inputstr1 = look_and_say(inputstr1)
print('part1: ',len(inputstr1))

for _ in range(10):
  inputstr1 = look_and_say(inputstr1)
print('part2: ',len(inputstr1))

print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')