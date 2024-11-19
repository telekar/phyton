with open ( "test.txt","r") as f:
    inputstr = f.read()

for n in range(len(inputstr)):
    inputList = inputstr.split("\n")

nice = 0

#def checkLetters(element):
count = 0


for element in inputList:
    print(element)
    pairs = []
    for i in range(len(element)-1):
        pairs.append(element[i] + element[i+1])
        print(pairs)

    

    for letters in pairs:
        print(letters)

        #if letters in element:
        #return True #is bad