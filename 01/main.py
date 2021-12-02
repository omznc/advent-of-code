import os


def getInput(filename: str) -> list[int]:
    tmp = []
    with open(
        os.path.dirname(os.path.realpath(__file__)) + f"\\{filename}", "r"
    ) as input_file:
        for line in input_file:
            tmp.append(int(line))
    return tmp


def parseWindows(input: list[int]) -> list[int]:
    temp = []
    try:
        for i in range(len(input)):
            temp.append(input[i] + input[i + 1] + input[i + 2])
    except IndexError:
        return temp


# Part 1
temp = measures = 0
for value in getInput("input1.txt"):
    if value > temp and temp != 0:
        measures += 1
    temp = value

print("Part 1 Solution: ", measures)

# Part 2
temp = measures = 0
for value in parseWindows(getInput("input2.txt")):
    if value > temp and temp != 0:
        measures += 1
    temp = value

print("Part 2 Solution: ", measures)
