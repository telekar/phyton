with open ( "test.txt","r") as f:
    inputstr = f.read()

for n in range(len(inputstr)):
    inputList = inputstr.split("\n")

print(inputList)

def checkLine(line):
    copy = line
    newLine = ""
    count = 0
    k=0
    line = line.replace('\\\\',"????")
    line = line.replace('\\x',"???")
    line = line.replace('\\"',"????")
    
    print(line)
    """for i in range(len(copy)+k):
        print("start:",len(copy))
        esc = (copy[i:i+2])
        if esc == '\\x':
            copy = copy[:i] + "???" + copy[i+2:]
            k += 1
            print(len(copy))
        elif esc == '\\"':
            copy = copy[:i] + "???" + copy[i+2:]
            print(len(copy))
        elif esc == '\\\\':
            copy = copy[:i] + "????" + copy[i+2:]
            k += 2
            print(len(copy))
            print(copy)
    """  
            
            
    return (line)
        

for line in inputList:
    nline = checkLine(line)
    print(nline)
    print (4+len(nline))