with open ( "puzzle_2a","r") as f:
    input = f.read()

reports = ()

countSave = 0
countSave2 = 0

for n in range(len(input)):
    reports = input.split("\n")

def checkLines(numbers):
    
    orientation = int(numbers[1]) - int(numbers[0]) #checking orientation of numbers
     
    if orientation == 0 or abs(orientation) >3: # checking differenc
        return False
        
    for i in range(1, len(numbers) - 1):
        diff = int(numbers[i+1]) - int(numbers[i])  #set orientation
        if diff * orientation <= 0:
            return False    #orientation has changed

        if abs(diff) == 0 or abs(diff) > 3: # checking differenc
            return False
    return True
        
def checkLines2(numbers):
    orientation = int(numbers[1]) - int(numbers[0])
    #print(numbers)
    
    if orientation == 0 or abs(orientation) >3: # checking differenc at beginning
        numbers = numbers[:1] + numbers[2:]     # delete wrong number
        #print(numbers)
        return (numbers)
      
        
    for i in range(1, len(numbers) - 1):
        diff = int(numbers[i+1]) - int(numbers[i])

        if diff * orientation <= 0: #orientation has changed
            numbers = numbers[:i+1] + numbers[i+2:] # delete wrong number
            #print(numbers)
            return (numbers)

        if abs(diff) == 0 or abs(diff) > 3:
            numbers = numbers[:i+1] + numbers[i+2:]
            print(numbers)
            return (numbers)
    return (numbers)

for level in reports:
    level = level.split()
    
    if checkLines(level):
        countSave += 1

    numbers = checkLines2(level)
    if numbers == level or checkLines(level):   # no change in numbers == good
        countSave2 += 1
    else:                                       # first change 
        if numbers == checkLines2(numbers):     # only one change == good
            countSave2 += 1

print("Part 1:",countSave)
print("Part 2:",countSave2)
