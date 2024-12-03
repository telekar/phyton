with open ( "puzzle_2a","r") as f:
    input = f.read()

levels = ()

countSave = 0
countSave2 = 0

for n in range(len(input)):
    levels = input.split("\n")

def checkLines(numbers):
    
    orientation = int(numbers[1]) - int(numbers[0])
    
    if orientation == 0 or abs(orientation) >3:
        return False
        
    for i in range(1, len(numbers) - 1):
        diff = int(numbers[i+1]) - int(numbers[i])
        if diff * orientation <= 0:
            return False

        if abs(diff) == 0 or abs(diff) > 3:
            return False
    return True
        
def checkLines2(numbers):
    orientation = int(numbers[1]) - int(numbers[0])
    print(numbers)
    
    if orientation == 0 or abs(orientation) >3:
        numbers = numbers[:1] + numbers[2:]
        print(numbers)
        if orientation == 0 or abs(orientation) >3:
            return (numbers)
      
        
    for i in range(1, len(numbers) - 1):
        diff = int(numbers[i+1]) - int(numbers[i])

        if diff * orientation <= 0:
            numbers = numbers[:i+1] + numbers[i+2:]
            print(numbers)
            return (numbers)

        if abs(diff) == 0 or abs(diff) > 3:
            numbers = numbers[:i+1] + numbers[i+2:]
            print(numbers)
            return (numbers)
    return (numbers)

for level in levels:
    level = level.split()
    
    if checkLines(level):
        countSave += 1

    numbers = checkLines2(level)
    if numbers == level or checkLines(level):
        countSave2 += 1
    else:
        if numbers == checkLines2(numbers):
            countSave2 += 1

print("Part 1:",countSave)
print("Part 2:",countSave2)
