import re

# 1D to 2D    
# x: idx / 1000
# y: idx % 1000 
# idx: x * width + y
board = [0] * 1000000

locationRegex = re.compile('\d{1,4},\d{1,4}')
dimensionsRegex = re.compile('\d{1,3}x\d{1,3}')

file = open('input.txt')

commands = file.read().split('\n')
commands.pop()

numGreaterThanEqualTwo = 0

for cmd in commands:
    # for coords and dims, first elem is x, second elem is y
    locMatch = locationRegex.search(cmd).group()
    coords = list(map(lambda x: int(x), locMatch.split(',')))
    dimMatch = dimensionsRegex.search(cmd).group()
    dims = list(map(lambda x: int(x), dimMatch.split('x')))
    
    for x in range(coords[0], coords[0] + dims[0]):
        for y in range(coords[1], coords[1] + dims[1]):
            board[x * 1000 + y] += 1
            if (board[x * 1000 + y] == 2):
                numGreaterThanEqualTwo += 1

for id, cmd in enumerate(commands):
    locMatch = locationRegex.search(cmd).group()
    coords = list(map(lambda x: int(x), locMatch.split(',')))
    dimMatch = dimensionsRegex.search(cmd).group()
    dims = list(map(lambda x: int(x), dimMatch.split('x')))

    overlapping = False
    for x in range(coords[0], coords[0] + dims[0]):
        for y in range(coords[1], coords[1] + dims[1]):
            if (board[x * 1000 + y] != 1):
                overlapping = True
                break
        if overlapping:
            break
    
    if not overlapping:
        print("id of non-overlapping:", id + 1)

print(numGreaterThanEqualTwo)