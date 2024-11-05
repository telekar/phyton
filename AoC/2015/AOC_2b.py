with open ( "puzzle_2a.txt","r") as f:
    pakets = f.read()

paketList = []
ribbon = 0

for n in range(len(pakets)):
    paketList = pakets.split("\n")

for n in range(len(paketList)):
    l,w,h = paketList[n].split('x')
    l = int(l)
    w = int(w)
    h = int(h)

    print (l,w,h)
    
    numbers = [l,w,h]
    numbers.sort()
    
    ribbon = ribbon + 2*numbers[0] + 2*numbers[1] + l*w*h

    print (ribbon)