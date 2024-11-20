with open ( "puzzle_6a.txt","r") as f:
#with open ( "test.txt","r") as f:   
    inputstr = f.read()

for n in range(len(inputstr)):
    inputList = inputstr.split("\n")

rows = 1000
words = ()

#define matrix
grid1 =[[0]*rows for i in range(rows)]
grid2 =[[0]*rows for i in range(rows)]

def fillGrid(x1,y1,x2,y2,cmd):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if cmd == "on":
                grid1[i][j] = 1
                grid2[i][j] += 1
            elif cmd == "off":
                grid1[i][j] = 0
                grid2[i][j] = grid2[i][j] -1
                if grid2[i][j] <0:
                    grid2[i][j] = 0
            else:
                grid1[i][j] = 1 - grid1[i][j]
                grid2[i][j] += 2
    return()
                
def sumGrid(grid):
    sum = 0
    for zeile in grid:
        for element in zeile:
            sum += element
    return sum

for line in inputList:
    words = line.split()
    x1,y1 = words[-3].split(",")
    x2,y2 = words[-1].split(",")
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    
    if "turn on" in line:
        fillGrid(x1,y1,x2,y2,"on")

    if "toggle" in line:
        fillGrid(x1,y1,x2,y2,"toggle")
        
    if "turn off" in line:
        fillGrid(x1,y1,x2,y2,"off")

print ("Part 1:", sumGrid(grid1))
print ("Part 2:",sumGrid(grid2))
