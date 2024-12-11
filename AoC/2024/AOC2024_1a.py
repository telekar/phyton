with open ( "puzzle_1a","r") as f:
    input = f.read()

lists = ()
left = ()
right = ()
sum1 = 0
sum2 = 0

for n in range(len(input)):
    lists = input.split("\n")

left = sorted([int(pair.split()[0]) for pair in lists])
right = sorted([int(pair.split()[1]) for pair in lists])

for n in range(len(left)):
    sum1 += (abs(left[n] - right[n]))

#part 1
print("Part 1 :",sum1)

for n in left:
    rightCount = right.count(n)
    sum2 += (rightCount*n)

#part2

print("Part 2 :",sum2)
