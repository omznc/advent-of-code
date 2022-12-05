values = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
data = [(line[:len(line) // 2], line[len(line) // 2:]) for line in open("input", "r").readlines()]

# Part 1
# One-liner
# print(sum(values.index(letter)+1 for letter in [[letter for letter in pair[0] if letter in pair[1]][0] for pair in [(line[:len(line) // 2], line[len(line) // 2:]) for line in open("input", "r").readlines()]]))

repeating = [[letter for letter in pair[0] if letter in pair[1]][0] for pair in data]

print(sum(values.index(letter)+1 for letter in repeating))

# Part 2
# One-liner
# (lambda data: print(sum(values.index(char) + 1 for char in [[letter for letter in group[0] if letter in group[1] and letter in group[2]][0] for group in [data[i:i + 3] for i in range(0, len(data), 3)]])))([line.strip() for line in open("input", "r").readlines()])

data = [line.strip() for line in open("input", "r").readlines()]
data = [data[i:i + 3] for i in range(0, len(data), 3)]
chars = [[letter for letter in group[0] if letter in group[1] and letter in group[2]][0] for group in data]

print(sum(values.index(char) + 1 for char in chars))
