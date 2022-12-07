import re

grid = list(open('input').read().splitlines()[:8])
grid = [line.ljust(len(max(grid, key=len))) for line in grid]
regex = re.compile(r"move (\d+) from (\d+) to (\d+)")
commands = open('input').read().splitlines()[10:]
stacks = [[] for _ in range(9)]

for element in grid:
    for i, stack in enumerate(re.compile(r"(.{3}) (.{3}) (.{3}) (.{3}) (.{3}) (.{3}) (.{3}) (.{3}) (.{3})").search(element).groups()):
        stacks[i].append(stack) if stack != '   ' else None

stacks = [stack[::-1] for stack in stacks]

# Part 1

for command in commands:
    num, from_, to = regex.search(command).groups()
    for _ in range(int(num)):
        try:
            stacks[int(to)-1].append(stacks[int(from_)-1].pop())
        except IndexError:
            break

print("".join([stack.pop() for stack in stacks if stack]).replace('[', '').replace(']', ''))


# Part 2

for command in commands:
    num, from_, to = regex.search(command).groups()
    try:
        stacks[int(to)-1] += stacks[int(from_)-1][-int(num):]
        stacks[int(from_)-1] = stacks[int(from_)-1][:-int(num)]
    except IndexError:
        break

print("".join([stack.pop() for stack in stacks if stack]).replace('[', '').replace(']', ''))

