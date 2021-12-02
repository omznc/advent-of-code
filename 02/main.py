import os

# Vertical, Horizontal & Aim Position
y = x = aim = 0


def parseCommand(command: str) -> tuple[str, int]:
    if "forward" in command:
        return ("forward", int(command[8:]))
    if "up" in command:
        return ("up", int(command[3:]))
    if "down" in command:
        return ("down", int(command[5:]))


def getInput(filename: str) -> list[str]:
    tmp = []
    with open(
        os.path.dirname(os.path.realpath(__file__)) + f"\\{filename}", "r"
    ) as input_file:
        for line in input_file:
            tmp.append(line.rstrip("\n"))
    return tmp


# Part One
for command in getInput("input1.txt"):
    p = parseCommand(command)
    match p[0]:
        case "forward":
            x += p[1]
        case "up":
            y -= p[1]
        case "down":
            y += p[1]

print(f"Part 1 Solution: {x * y}")

# Part Two
x = y = aim = 0

for command in getInput("input2.txt"):
    p = parseCommand(command)
    match p[0]:
        case "forward":
            x += p[1]
            y += aim * p[1]
        case "up":
            aim -= p[1]
        case "down":
            aim += p[1]

print(f"Part 2 Solution: {x*y}")
