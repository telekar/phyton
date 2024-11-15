with open ( "puzzle_5a.txt","r") as f:
    inputstr = f.read()

for n in range(len(inputstr)):
    inputList = inputstr.split("\n")

nice = 0

def checkLetters(element):
    count = 0
    verbose = ("ab","cd","pq","xy")

    for letters in verbose:
        if letters in element:
            return True #is bad
    return False

def findDouble(element):
    for i in range(len(element)-1):
        if element[i] == element[i+1]:
            return True #is good
    return False

def countVowels(element):
    vowels = "aeiou"
    count = 0
    for i in element:
        if i in vowels:
            count += 1
    if count >= 3:
       return True  #is good
    return False


for element in inputList:
    if checkLetters(element):
        continue

    if not findDouble(element):
        continue

    if not countVowels(element):
        continue

    nice = nice +1  
    
print(nice)
  

