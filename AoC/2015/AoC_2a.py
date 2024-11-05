with open ( "puzzle_2a.txt","r") as f:
    pakets = f.read()

paketList = []
squareSum = 0

for n in range(len(pakets)):
    paketList = pakets.split("\n")

for n in range(len(paketList)):
    l,w,h = paketList[n].split('x')
    l = int(l)
    w = int(w)
    h = int(h)

    a = l * w
    b = l * h
    c = w * h

    squareTemp = 2*a + 2*b +2*c
    lowest = min(a,b,c)
    squareSum = squareSum + squareTemp + lowest

print (squareSum)
