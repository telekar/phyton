import re
lines = []
with open ( "test","r") as f:
    for line in f.readlines():
        x,y = (int(z) for z in line.split())

print (x,y)

def findMul(input):
    muster = r"mul\(([\d]+),([\d]+)\)"
    treffer = re.findall(muster, input)
    return treffer

sum1 = 0

for Line in lines:
    #print(Line)
    mulList = findMul(Line)
    print(mulList)
   
    for mult in mulList:
        a,b = mult
        sum1 += int(a)*int(b)

print('Part1:',sum1)