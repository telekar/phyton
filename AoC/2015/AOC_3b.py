with open ( "puzzle_3a.txt","r") as f:
    directions = f.read()

floorX = []             # X = Xmen ; R = Robot
floorR = []

xX = xR =0  
yX = yR =0

koordX = koordR = xX,yX

floorX.append(koordX)
#floorR.append(koordR)

for n in range(len(directions)):
#for n in range(40):
    print(n,directions[n])
    if n % 2 == 0:      #xmen move
        if directions[n] == "^":
            yX = yX - 1
            if (xX,yX) not in floorX:
                koordX = xX,yX
                floorX.append(koordX)
                #print (n,directions[n],floorX)
        if directions[n] == "<":
            xX = xX - 1
            if (xX,yX) not in floorX:
                koordX = xX,yX
                floorX.append(koordX)
                #print (n,directions[n],floorX)
        if directions[n] == "v":
            yX = yX + 1
            if (xX,yX) not in floorX:
                koordX = xX,yX
                floorX.append(koordX)
                #print (n,directions[n],floorX)
        if directions[n] == ">":
            xX = xX + 1
            if (xX,yX) not in floorX:
                koordX = xX,yX
                floorX.append(koordX)
                #print (n,directions[n],floorX)
    
    if n % 2 == 1:      #Robot move
        if directions[n] == "^":
            yR = yR - 1
            if (xR,yR) not in floorX:
                koordR = xR,yR
                floorX.append(koordR)
                #print (n,directions[n],floorR)
        if directions[n] == "<":
            xR = xR - 1
            if (xR,yR) not in floorX:
                koordR = xR,yR
                floorX.append(koordR)
                #print (n,directions[n],floorR)
        if directions[n] == "v":
            yR = yR + 1
            if (xR,yR) not in floorX:
                koordR = xR,yR
                floorX.append(koordR)
                #print (n,directions[n],floorR)
        if directions[n] == ">":
            xR = xR + 1
            if (xR,yR) not in floorX:
                koordxR = xR,yR
                floorX.append(koordR)
                #print (n,directions[n],floorR)
einzigartige_elemente = set(floorX)
print(len(einzigartige_elemente))
doppelte_elemente = list(set(floorX) - set(einzigartige_elemente))
print(doppelte_elemente)
#print(len(floorX))


