
pairs = {'X': 'A', 'Y': 'B', 'Z': 'C'}
beats = {'A': 'C', 'B': 'A', 'C': 'B'}

data = [[a[0], pairs[a[1]]] for a in [list(line.strip().split(' ')) for line in open('input')]]

# Part 1

# One-liner
# score = sum((6 if beats[move[1]] == move[0] else 3 if move[1] == move[0] else 0) + ["A", "B", "C"].index(move[1]) + 1 for move in data)

score = 0
for move in data:
    if beats[move[1]] == move[0]:
        score += 6
    elif move[1] == move[0]:
        score += 3
    else:
        score += 0
    score += ["A", "B", "C"].index(move[1]) + 1

print(score)

# Part 2

# One-liner
# score = sum((0 + ["A", "B", "C"].index(beats[move[0]]) + 1) if move[1] == 'A' else (3 + ["A", "B", "C"].index(move[0]) + 1) if move[1] == 'B' else (6 + ["A", "B", "C"].index(beatby[move[0]]) + 1) for move in data)

score = 0
for move in data:
    match move[1]:
        case 'A':
            score += 0 + ["A", "B", "C"].index(beats[move[0]]) + 1
        case 'B':
            score += 3 + ["A", "B", "C"].index(move[0]) + 1
        case 'C':
            score += 6 + ["A", "B", "C"].index(beats[beats[move[0]]]) + 1

print(score)



