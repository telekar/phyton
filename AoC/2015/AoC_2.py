# calculating the required wrapping paper for each gift a little easier: 
# find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. 
# The elves also need a little extra paper for each present: the area of the smallest side.

# The ribbon required to wrap a present is the shortest distance around its sides, 
# or the smallest perimeter of any one face.
# the feet of ribbon required for the perfect bow is 
# equal to the cubic feet of volume of the present.

with open ( "puzzle2.txt","r") as f:
    pakets = f.read()

paketList = []
squareSum = 0
ribbon = 0
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

    numbers = [l,w,h]
    numbers.sort()
    
    ribbon = ribbon + 2*numbers[0] + 2*numbers[1] + l*w*h

print ('Part 1:',squareSum)
print ('Part 2:',ribbon)