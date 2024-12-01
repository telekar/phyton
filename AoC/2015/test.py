distances = {}
citiList = set ()
with open ('test.txt', 'r') as f:
    for line in f:
        cities, distance = line.split(' = ')
        city1, city2 =cities.split(' to ')
        citiList.add(city1)
        citiList.add(city2)
        distances[(city1, city2)] = int(distance)
        print (city1,city2,distance)

print(citiList)

def find_combinations(cities, r):
  """Findet alle Kombinationen von r Städten aus einer Liste.

  Args:
    cities: Eine Liste von Städten.
    r: Die Anzahl der Städte in jeder Kombination.

  Returns:
    Eine Liste aller möglichen Kombinationen.
  """

  result = []
  if r == 0:
    return [[]]
  for i in range(len(citiList)):
    rest = citiList[:i] + citiList[i+1:]
    for c in find_combinations(rest, r-1):
      result.append([citiList[i]] + c)
  return result

print (find_combinations(citiList,len(citiList)))

