from itertools import combinations
data = [line.split(',') for line in open('input').read().splitlines()]

# Both parts
overlaps, anyOverlaps = 0, 0
for group in data:
    for pair in combinations(group, 2):
        beginning , end = pair[0].split('-')
        beginning2, end2 = pair[1].split('-')
        overlaps += int(int(beginning) <= int(beginning2) and int(end) >= int(end2)) or (int(beginning2) <= int(beginning) and int(end2) >= int(end))
        anyOverlaps += int(int(beginning) <= int(beginning2) <= int(end)) or (int(beginning2) <= int(beginning) <= int(end2))

print(overlaps, anyOverlaps)

