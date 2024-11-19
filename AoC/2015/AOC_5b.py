with open ( "puzzle_5a.txt","r") as f:
    inputstr = f.read()

for n in range(len(inputstr)):
    inputList = inputstr.split("\n")

nice = 0

def checkpairs(element):
    pairs = []
    for i in range(len(element)-1):
        pairs.append(element[i] + element[i+1])
    
    for pair in pairs:
        if findDouble(element,pair):
            return True
        
def overlapp(element):
    for i in range(len(element)-1):
        if element[i:i+2] == element[i+1:i+3]:
            return False    #overlapp
    return True             #no overlapp

def findDouble(element,pair):
    count = 0
    for i in range(len(element)-1):
        
        if element[i:i+2] == pair:
            count += 1
            if count > 1:
                return True #found douple
            
    return ()

def checkLetters(element):
    for i in range(len(element)-2):
        if element[i] == element[i+2] and element[i] != element[i+1]:
            return True # one letter between same letters



for element in inputList:
    if not overlapp(element):
        continue

    if not checkpairs(element):
        continue

    if not checkLetters(element):
        continue

    nice += 1  
    
print(nice)
  

