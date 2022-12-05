
# One-liner
#(lambda i: print(i[0], sum(i)))(__import__('heapq').nlargest(3, [sum(int(item) for item in group.splitlines()) for group in open('input').read().split('\n\n')]))

data = open('input').read().split('\n\n')
groups = [sum(int(item) for item in group.splitlines()) for group in data]

# Part 1
print(max(groups))

# Part 2
print(sum(__import__('heapq').nlargest(3, groups)))

