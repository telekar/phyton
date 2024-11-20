import numpy as np
import re

with open ( "puzzle_6a.txt","r") as f:
#with open ( "test.txt","r") as f:   
    inputstr = f.read()

for n in range(len(inputstr)):
    inputList = inputstr.split("\n")

matrix = np.zeros((1000,1000))
list = ()

def extractKoords(string):

  pattern = r"(\d+),(\d+)\s+through\s+(\d+),(\d+)"
  match = re.search(pattern, string)

  if match:
    x1, y1, x2, y2 = map(int, match.groups())
    return [(x1, y1), (x2, y2)]
  else:
    return None
   

for element in inputList:
    if "turn on" in element:
        list = extractKoords(element)
        x1,y1 = list[0]
        x2,y2 = list[1]
        matrix[x1:x2+1, y1:y2+1] = 1

    if "toggle" in element:
        list = extractKoords(element)
        x1,y1 = list[0]
        x2,y2 = list[1]
        matrixCopy = matrix[x1:x2+1, y1:y2+1].copy()
        matrixCopy = np.logical_not(matrixCopy)
        matrixCopy = matrixCopy.astype(int)
        matrix[x1:x2+1, y1:y2+1] = matrixCopy
        
    if "turn off" in element:
        list = extractKoords(element)
        x1,y1 = list[0]
        x2,y2 = list[1]
        matrix[x1:x2+1, y1:y2+1] = 0

mask = matrix == 1
print(np.sum(mask))
#print(matrix)