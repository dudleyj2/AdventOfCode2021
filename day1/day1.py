# Day 1 Part 1
with open('input.txt') as f:
    contents = f.readlines()

int_contents = [int(c) for c in contents]

increase = 0
for i in range(len(int_contents) - 1):
    if int_contents[i+1] > int_contents[i]:
        increase += 1

print(f'Part 1: {increase}')

# Day 2 Part 2

# get measurement window lists
windows = []
for i in range(len(int_contents) - 2):
    windows.append(
        [int_contents[i], int_contents[i+1], int_contents[i+2]]
    )

increase = 0
for i in range(len(windows) - 1):
    if sum(windows[i+1]) > sum(windows[i]):
        increase += 1

print(f'Part 2: {increase}')
