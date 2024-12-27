import time, re

part1 = part2 = 0

with open ( "test","r") as f:
    input = f.readlines()

  
print(input)



time_start = time.perf_counter()


#print(f'Solution: {solve(load("test"))}')
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')