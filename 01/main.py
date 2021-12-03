# The setup for this problem
# https://adventofcode.com/2021/day/1

import os

BOLD, END = "\033[1m", "\033[0m"


def getInput(filename: str) -> list[int]:
    tmp = []
    with open(os.path.dirname(os.path.realpath(__file__)) + f"\\{filename}", "r") as f:
        return list(map(int, f.read().split("\n")))


def parseWindows(input: list[int]) -> list[int]:
    return [
        input[i] + input[i + 1] + input[i + 2]
        for i in range(len(input))
        if len(input) - i > 2
    ]


# Part 1
tmp = measures = 0
for value in getInput("input1.txt"):
    if value > tmp and tmp != 0:
        measures += 1
    tmp = value

print(f"1/2: {BOLD}{measures}{END}")

# Part 2
tmp = measures = 0
for value in parseWindows(getInput("input2.txt")):
    if value > tmp and tmp != 0:
        measures += 1
    tmp = value

print(f"2/2: {BOLD}{measures}{END}")
