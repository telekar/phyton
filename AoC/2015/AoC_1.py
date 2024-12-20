# He starts on the ground floor (floor 0) and 
# then follows the instructions one character at a time.

# An opening parenthesis, (, means he should go up one floor, and 
# a closing parenthesis, ), means he should go down one floor.

# find the position of the first character that causes him to enter 
# the basement (floor -1). The first character in the instructions has position 1, 
# the second character has position 2, and so on.

with open ( "puzzle1.txt","r") as f:
    direction = f.read()

floor = 0
partB = True

for n in range(len(direction)):
    sign = direction[n]

    if sign == "(":
        floor += 1
    if sign == ")":
        floor -= 1
        if floor == -1 and partB == True:
            pos = n+1
            partB = False
print ('Part 1: ',floor)
print ('Part 2: ',pos)