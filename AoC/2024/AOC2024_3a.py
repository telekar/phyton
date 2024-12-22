import re
lines = []

with open ( "puzzle_3a","r") as f:
    input = f.read()

for n in range(len(input)):
    lists = input.split("\n")

def findMul(input):
    muster = r"mul\(([\d]+),([\d]+)\)"
    treffer = re.findall(muster, input)
    return treffer

sum1 = 0

for Line in lists:
    mulList = findMul(Line)
    
   
    for mult in mulList:
        a,b = mult
        sum1 += int(a)*int(b)

print('Part1:',sum1)
