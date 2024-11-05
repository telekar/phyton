with open ( "puzzle_1a.txt","r") as f:
    direction = f.read()

floor = 0

for n in range(len(direction)):
    sign = direction[n]

    if sign == "(":
        floor += 1
    if sign == ")":
        floor -= 1
print (floor)