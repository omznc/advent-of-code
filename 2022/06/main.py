data = [line.strip() for line in open("input", "r").readlines()][0]

# Day 1
# One-liner
# print([i for i in range(len(data)) if len(set(data[i:i+4])) == 4][0] + 4)

# Day 2
# One-liner
# print([i for i in range(len(data)) if len(set(data[i:i+14])) == 14][0] + 14)

# Both days, one loop
solution, solution2 = 0, 0
for i in range(len(data)):
    if solution and solution2:
        break
    if not solution and len(set(data[i:i+4])) == 4:
        solution = i + 4
    if not solution2 and len(set(data[i:i+14])) == 14:
        solution2 = i + 14

print(solution, solution2)
