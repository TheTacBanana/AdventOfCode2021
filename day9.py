import math

grid = []

with open("input.txt") as f:
    grid = [i.strip() for i in f.readlines()]
    grid = [[int(grid[i][j]) for j in range(len(grid[i]))] for i in range(len(grid))]

suml = 0

basin_count = 0
basins = {}

for y in range(len(grid)):
    for x in range(len(grid[y])):
        height = grid[y][x]
        if ((x == 0 or grid[y][x-1] > height) and
            (x == len(grid[y]) - 1 or grid[y][x+1] > height) and
            (y == 0 or grid[y-1][x] > height) and
            (y == len(grid) - 1 or grid[y+1][x] > height)):
            suml += height + 1

            basins[(x, y)] = basin_count
            basin_count = basin_count + 1

finished = False

while not finished:
    finished = True
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            height = grid[y][x]
            
            if (x, y) in basins:
                continue

            if (x-1, y) in basins and height != 9:
                basins[(x, y)] = basins[(x-1, y)]
                finished = False
            if (x+1, y) in basins and height != 9:
                basins[(x, y)] = basins[(x+1, y)]
                finished = False
            if (x, y-1) in basins and height != 9:
                basins[(x, y)] = basins[(x, y-1)]
                finished = False
            if (x, y+1) in basins and height != 9:
                basins[(x, y)] = basins[(x, y+1)]
                finished = False

basin_size = [0] * basin_count

for basin in basins.values():
    basin_size[basin] = basin_size[basin] + 1

print(suml)
print(math.prod(sorted(basin_size)[-3:]))