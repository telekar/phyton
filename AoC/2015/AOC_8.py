with open ( "puzzle8.txt","r") as f:
    inputstr = f.read()

for n in range(len(inputstr)):
    inputList = inputstr.split("\n")

def replace(line):
    
    line = line.replace('\\\\',"????")
    line = line.replace('\\x',"???")
    line = line.replace('\\"',"????")
    return(line)

sumChar = 0
sumEsc = 0
sumNew = 0

for line in inputList:
    lenLine = len(line)
    sumChar += lenLine
    lenEsc = len(eval(line))
    sumEsc += lenEsc
    
    nline = replace(line)

    sumNew += len(nline) +4

#part1
print ('Part 1:',sumChar-sumEsc)

#part2
print ('Part 2:',sumNew-sumChar)
    