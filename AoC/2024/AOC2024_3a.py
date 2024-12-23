import re
lines = []

#with open ( "test3","r") as f:
with open ( "puzzle_3a","r") as f:
    input = f.read()

for n in range(len(input)):
    lists = input.split("\n")

def findMul(input):
    #found all multiplications
    muster = r"mul\(([\d]+),([\d]+)\)"
    #found all mul, do and dont
    muster2 = r"do\(\)|don\'t\(\)|mul\(\d+,\d+\)"

    treffer = re.findall(muster, input)
    #print(treffer)
    treffer2 = re.findall(muster2, input)
    #print(treffer2)
    return treffer, treffer2

sum1 = 0
sum2 = 0
doMul = []
doIt = True
for Line in lists:
    mulList1,mulList2 = findMul(Line)
    
    for mult in mulList1:
       a,b = mult
       sum1 += int(a)*int(b)

    for i in range(len(mulList2)):
        #print("multilisti: ",mulList2[i])
        if mulList2[i] == "don't()":    #switch to dont
            doIt = False
            continue
        elif mulList2[i] == "do()":     #switch to do
            doIt = True
            continue
        else:
            if doIt == True:                       
                doMul.append(mulList2[i])   #append all mul if do is enabled
                #print(doMul)
            
    for found in doMul:
        #print(found)
        match = re.findall(r"mul\(([\d]+),([\d]+)\)", found)
        c,d = (match[0])
        sum2 += int(c) * int(d)

print('Part1:',sum1)
print('Part2:',sum2)