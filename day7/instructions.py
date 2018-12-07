from collections import defaultdict
from collections import deque
from sortedcontainers import SortedSet

with open('input.txt') as f:
    cmds = f.read().splitlines()

# Graph is a graph of directed nodes to adjacent vertices
graph = defaultdict(list)

# Prereqs is a graph of every node and its prerequisites
prereqs = defaultdict(list)
allNodes = set()

for cmd in cmds:
    # Luckily all the node names are in the same index in every command
    pre = cmd[5]
    post = cmd[36]
    graph[pre].append(post)
    graph[post]                     # This initializes the end node of the graph (as it will have no adj edges)

    prereqs[pre]
    prereqs[post].append(pre)


visited = set()
allNodes = set(graph.keys())

# Start nodes have zero incoming edges
startNodes = list(map(lambda x: x[0], filter(lambda x: len(x[1]) == 0, prereqs.items())))
print(startNodes)

# All nodes adjacent to our current subgraph
adjacents = SortedSet(startNodes)

answer = []
startNode = adjacents[0]
visited.add(startNode)

while visited != allNodes:
    # The next node we visit is the 1. the first in the alphabet 2. whose prereqs have all been visited.
    # We represent this by checking each possible node's prereqs and seeing if it is a subset of the
    # visited set.
    idx = 0
    while not (SortedSet(prereqs[adjacents[idx]]) <= visited):
        idx += 1
    
    nextNode = adjacents.pop(idx)
    visited.add(nextNode)

    adjacents.update(graph[nextNode])
    answer.append(nextNode)

answer = ''.join(answer)

answerFile = open('part1output.txt', 'w')
answerFile.write(answer)

assert len(answer) == len(visited)

print(answer)
