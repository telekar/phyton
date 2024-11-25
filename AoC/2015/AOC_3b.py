with open ( "puzzle_3a.txt","r") as f:
    directions = f.read()

floorX = []             # X = Xmen ; R = Robot
floorR = []

xX = xR =0  
yX = yR =0

koordX = koordR = xX,yX

floorX.append(koordX)

for n in range(len(directions)):
    print(n,directions[n])
    if n % 2 == 0:      #xmen move
        if directions[n] == "^":
            yX = yX - 1
            if (xX,yX) not in floorX:
                koordX = xX,yX
                floorX.append(koordX)
        if directions[n] == "<":
            xX = xX - 1
            if (xX,yX) not in floorX:
                koordX = xX,yX
                floorX.append(koordX)
        if directions[n] == "v":
            yX = yX + 1
            if (xX,yX) not in floorX:
                koordX = xX,yX
                floorX.append(koordX)
        if directions[n] == ">":
            xX = xX + 1
            if (xX,yX) not in floorX:
                koordX = xX,yX
                floorX.append(koordX)
    
    else: #if n % 2 == 1:      #Robot move
        if directions[n] == "^":
            yR = yR - 1
            if (xR,yR) not in floorX:
                koordR = xR,yR
                floorX.append(koordR)
        if directions[n] == "<":
            xR = xR - 1
            if (xR,yR) not in floorX:
                koordR = xR,yR
                floorX.append(koordR)
        if directions[n] == "v":
            yR = yR + 1
            if (xR,yR) not in floorX:
                koordR = xR,yR
                floorX.append(koordR)
        if directions[n] == ">":
            xR = xR + 1
            if (xR,yR) not in floorX:
                koordR = xR,yR
                floorX.append(koordR)
    print (len(floorX))


