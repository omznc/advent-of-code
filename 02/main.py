# The setup for this problem
# https://adventofcode.com/2021/day/2

import os

BOLD, END = "\033[1m", "\033[0m"


def getInput(filename: str) -> list[tuple[str, int]]:
    with open(os.path.dirname(os.path.realpath(__file__)) + f"\\{filename}", "r") as f:
        return [(x[0], int(x[1])) for x in [x.split(" ") for x in f.read().split("\n")]]


# Part One
y = x = aim = 0

for command in getInput("input1.txt"):
    match command[0]:
        case "forward":
            x += command[1]
        case "up":
            y -= command[1]
        case "down":
            y += command[1]

print(f"1/2: {BOLD}{x * y}{END}")

# Part Two
x = y = aim = 0

for command in getInput("input2.txt"):
    match command[0]:
        case "forward":
            x += command[1]
            y += aim * command[1]
        case "up":
            aim -= command[1]
        case "down":
            aim += command[1]

print(f"2/2: {BOLD}{x * y}{END}")
