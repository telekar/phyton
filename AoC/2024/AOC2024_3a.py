import re

with open ( "puzzle_3a","r") as f:
    lines = f.readlines()

doIt = True
sum1 = 0
sum2 = 0

for line in lines:
    lists = re.findall("mul\\(\\d+,\\d+\\)|do\\(\\)|don\\'t\\(\\)", line)
    
    for command in lists:
        if command == "do()":
            doIt = True
            continue
        if command == "don't()":
            doIt = False
            continue
        if doIt == True:
            numbers = list(map(int, re.findall("\\d+",command)))
            sum2 += numbers[0] * numbers[1]
       
        if doIt == False:
            numbers = list(map(int, re.findall("\\d+",command)))
            sum1 +=  numbers[0] * numbers[1]

print("Part 1: ",sum1 + sum2)
print("Part 2: ",sum2)
