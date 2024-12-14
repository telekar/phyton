# turn on 0,0 through 999,999 would turn on (or leave on) every light.
# toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
# turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
# After following the instructions, how many lights are lit?

# The phrase turn on actually means that you should increase the brightness of those lights by 1.
# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.
# The phrase toggle actually means that you should increase the brightness of those lights by 2.

# What is the total brightness

with open ( "puzzle6.txt","r") as f:  
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
    x1,y1 = map(int,words[-3].split(","))
    x2,y2 = map(int,words[-1].split(","))
   
    
    if "turn on" in line:
        fillGrid(x1,y1,x2,y2,"on")

    if "toggle" in line:
        fillGrid(x1,y1,x2,y2,"toggle")
        
    if "turn off" in line:
        fillGrid(x1,y1,x2,y2,"off")

print ("Part 1:", sumGrid(grid1))
print ("Part 2:",sumGrid(grid2))
