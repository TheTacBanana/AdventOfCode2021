from typing import DefaultDict

with open("input.txt") as f:
    file = f.readlines()
    nodes = []
    for line in file:
        nodeLine = []
        for c in line.strip():
            nodeLine.append(int(c))

        nodes.append(nodeLine)

def ConvertNum(i):
    if i > 9: i -= 9
    return i

part2 = True

if part2:
    originalSize = len(nodes)
    for row in range(originalSize):
        for i in range(4):
            for col in range(originalSize):
                integer = int(nodes[row][col]) + i + 1
                nodes[row].append(ConvertNum(integer))
    for j in range(1,5):
        for row in range(originalSize):
            nodes.append([ConvertNum(int(i) + j) for i in nodes[row]])

adjacencyDict = DefaultDict(list)
paths = []

for row in range(len(nodes)):
    for col in range(len(nodes[row])):
        rctuple = (row,col)
        if col != 0:
            adjacencyDict[rctuple].append((row,col-1))
        if row != 0:
            adjacencyDict[rctuple].append((row-1,col))
        if col != len(nodes[row]) - 1:
            adjacencyDict[rctuple].append((row,col+1))
        if row != len(nodes) - 1:
            adjacencyDict[rctuple].append((row+1,col))

openNodes = DefaultDict()
openNodes[(0,0)] = 0
closedNodes = DefaultDict()

removeFromOpenList = []

finished = False
while not finished:
    shortestTravel = []
    for node in openNodes:
        curCount = openNodes[node]
        closedCount = 0
        for adjacent in adjacencyDict[node]:
            if adjacent not in openNodes and adjacent not in closedNodes:
                n = nodes[adjacent[0]][adjacent[1]]
                shortestTravel.append((adjacent,curCount + int(n)))
            else:
                closedCount += 1
        if closedCount == len(adjacencyDict[node]):
            removeFromOpenList.append(node)

    for node in removeFromOpenList:
        closedNodes[node] = openNodes[node]
        openNodes.pop(node)
    removeFromOpenList = []

    if len(shortestTravel) != 0:
        shortestTravel.sort(key=lambda x:x[1])
        openNodes[shortestTravel[0][0]] = shortestTravel[0][1]
    else:
        finished = True

print(closedNodes[(len(nodes) - 1, len(nodes[0]) - 1)])