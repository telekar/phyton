# A nice string is one with all of the following properties:

# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

with open ( "puzzle5.txt","r") as f:
    inputstr = f.read()

for n in range(len(inputstr)):
    inputList = inputstr.split("\n")

nice = 0

def checkLetters(element):
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

    nice = nice + 1  
    
print(nice)
  

