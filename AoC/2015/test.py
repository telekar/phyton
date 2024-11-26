distances = {}

with open ('test.txt', 'r') as f:
    for line in f:
        cities, distance = line.split(' = ')
        city1, city2 =cities.split(' to ')
        distances[(city1, city2)] = int(distance)
        print (city1,city2,distance)
print(distances)