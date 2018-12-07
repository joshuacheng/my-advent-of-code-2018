import sys
from collections import defaultdict

file = open('input.txt')
points = file.read().split('\n')
points.pop()

def split(pointStr):
    arr = pointStr.split(', ')
    return (int(arr[0]), int(arr[1]))

points = list(map(split, points))
#print(points)

# Sort by x and y
pointsSortedByX = sorted(points, key=lambda x: x[0])
pointsSortedByY = sorted(points, key=lambda x: x[1])

lowestX = pointsSortedByX[0][0]
highestX = pointsSortedByX[len(pointsSortedByX) - 1][0]
lowestY = pointsSortedByY[0][1]
highestY = pointsSortedByY[len(pointsSortedByY) - 1][1]

print(lowestX, highestX, lowestY, highestY)

pointAreaDict = defaultdict(int)
pointAreaDict2 = defaultdict(int)

# See Manhattan Distance
def mDist(pt1, pt2):
    return abs(pt1[0]-pt2[0]) + abs(pt1[1] - pt2[1])

# Return closest point from array to pt1
# If two points have the same distance, return some other sentient value
def closestPt(pt1, ptArr):
    min = sys.maxsize
    secondMin = sys.maxsize
    for pt in ptArr:
        curr = mDist(pt1, pt)
        if curr < min:
            secondMin = min
            min = curr
            minPt = pt
        elif curr == min:
            secondMin = min
    
    if secondMin == min:
        return 'same'
    return minPt


###                   PART 1                   ###
# Any points who own closest points that are along our border should be eliminated from
# consideration because they will own infinite closest points. They will be added
# to this set.
# Weak proof: If they own at least one point on the border, they own all points in a straight line
#             out to infinity
borderOwners = set()

# Brute force O(n^2) because I'm not sure what algorithm to use.
# Nearest Neighbor maybe? but where do I get my kd-tree
# for x in range(lowestX, highestX):
#     for y in range(lowestY, highestY):
#         closePt = closestPt((x, y), points)
#         if closePt == 'same':
#             continue
#         else:
#             if x == lowestX or x == highestX - 1 or y == lowestY or y == highestY - 1:
#                 borderOwners.add(closePt)
#             pointAreaDict[closePt] += 1

# largestArea = list(filter(lambda x: x[0] not in borderOwners, sorted(pointAreaDict.items(), key=lambda x: x[1], reverse=True)))[0][1]
# print(largestArea)

# Part 2

def sumDistances(coord, pts):
    total = 0
    for point in pts:
        total += mDist(coord, point)

    return total

area = 0
for x in range(lowestX, highestX):
    for y in range(lowestY, highestY):
        if sumDistances((x, y), points) < 10000:
            area += 1

print(area)