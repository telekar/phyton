from itertools import permutations

distances = {}
towns = set()

with open ( "puzzle_9a.txt","r") as f:
   for line in f.readlines():
        left, right = line.strip().split(' = ')
        dist = int(right)
        town1,town2 = left.split(' to ')
        distances[(town1,town2)] = dist
        distances[(town2,town1)] = dist
        towns.add(town1)
        towns.add(town2)

shortest = 999999
longest = 0
for route in permutations(towns):
    temp = 0
    for i in range(len(route)-1):
        temp += distances[(route[i],route[i+1])]
    if temp <= shortest:
        shortest = temp
    if temp >= longest:
        longest = temp         

print('Part1: ',shortest)
print('Part2: ',longest)