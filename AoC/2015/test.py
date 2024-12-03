import itertools

distances = {}
citiList = set ()
routeList = ()

with open ('test.txt', 'r') as f:
    for line in f:
        cities, distance = line.split(' = ')
        city1, city2 =cities.split(' to ')
        citiList.add(city1)
        citiList.add(city2)
        distances[(city1, city2)] = int(distance)
        distances[(city2, city1)] = int(distance)
        print (city1,city2,distance)

#print(citiList)
print(distances)
routs = list(itertools.permutations(citiList))

städte = list(distances.keys())
min_distance = float('inf')
next_city = ()
for start in städte:
    current_distance = 0
    current_city = start
    for _ in range(len(städte)-1):
        min_dist = float('inf')
        for city in städte:
            if city != current_city and (current_city,city) in distances:
                if distances[(current_city,city)] < min_dist:
                    min_dist = distances[(current_city,city)]
                    next_city = city
        current_distance += min_dist
        
        current_city = next_city
        print(current_distance,current_city)
    if current_distance < min_distance:
        min_distance = current_distance
        shortest_route = start

#print(shortest_route) 
#print(min_distance) 
            

print (städte)