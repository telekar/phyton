# this is not my Solution, because is from other Youtuber "HexTree"

reports = []

with open('puzzle_2a', 'r') as f:
    for line in f.readlines():
        reports.append([int(z) for z in line.split()])

def is_safe(l):
    n = len(l)
    return ((all(1 <= l[i+1] - l[i] <= 3 for i in range(n-1))) or (all(1 <= l[i] - l[i+1] <= 3 for i in range(n-1))))

safe_count = sum(map(is_safe,reports))

print('part1:', safe_count)

safe_count2 = 0
for report in reports:
    safe_count2 += is_safe(report) or any(is_safe(report[:i] + report[i+1:]) for i in range(len(report)))

print('part2:', safe_count2)