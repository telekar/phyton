# Moves are always exactly one house to the 
# north (^), south (v), east (>), or west (<). 
# After each move, he delivers another present to the house at his new location.

# How many houses receive at least one present?

with open ( "puzzle3.txt","r") as f:
    directions = f.read()

floor = []
x=0
y=0
koord = x,y
floor.append(koord)

for n in range(len(directions)):

  if directions[n] == "^":
    y = y - 1
    if (x,y) not in floor:
      koord = x,y
      floor.append(koord)
  if directions[n] == "<":
    x = x - 1
    if (x,y) not in  floor:
      koord = x,y
      floor.append(koord)
  if directions[n] == "v":
    y = y + 1
    if (x,y) not in  floor:
      koord = x,y
      floor.append(koord)
  if directions[n] == ">":
    x = x + 1
    if (x,y) not in  floor:
      koord = x,y
      floor.append(koord)

print('Part 1:',len(floor))


