from types import CodeType
from typing import DefaultDict
from copy import copy

with open("input.txt") as f:
    arcs = [i.strip().split("-") for i in f.readlines()]

adjacencyDict = DefaultDict(list)
paths = []
maxMinCaves = 1
doubleVisited = False

for arc in arcs:
    adjacencyDict[arc[0]].append(arc[1])
    adjacencyDict[arc[1]].append(arc[0])

print(adjacencyDict)

def AllPathsSub(s, d, visited, path):
    visited[s] += 1
    path.append(s)

    if s == d:
        if tuple(path) not in paths:
            paths.append(tuple(copy(path)))
    else:
        for i in adjacencyDict[s]:
            if i.isupper() or visited[i] < maxMinCaves:
                AllPathsSub(i, d, visited, path)

    path.pop()
    visited[s] -= 1

def AllPaths(s, d):
    dictKeys = adjacencyDict.keys()

    lowerArcs = [i for i in dictKeys if i.islower() and i not in ["start", "end"]]
    print(lowerArcs)

    path = []
    for arc in lowerArcs:
        visited = DefaultDict(int)
        for key in dictKeys:
            if key == arc:
                visited[key] = -1
            else:
                visited[key] = 0

        visited["start"] = maxMinCaves
        visited["end"] = maxMinCaves - 1

        print(visited)
    
        AllPathsSub(s, d, copy(visited), path)

count = 0

AllPaths("start", "end")
for arc in arcs2:
    if tuple(arc) not in paths:
        print(tuple(arc))
    else:
        print("Found: ", tuple(arc))

print(len(paths), count)
