with open("input.txt") as f:
    grid = [i.strip() for i in f.readlines()]
    grid = [[int(grid[i][j]) for j in range(len(grid[i]))] for i in range(len(grid))]

suml = 0
basins = {}
totalBasins = 0

for y in range(len(grid)):
    for x in range(len(grid[y])):
        height = grid[y][x]
        if ((x == 0 or grid[y][x-1] > height) and
            (x == len(grid[y]) - 1 or grid[y][x+1] > height) and
            (y == 0 or grid[y-1][x] > height) and
            (y == len(grid) - 1 or grid[y+1][x] > height)):
            #suml += height + 1

            basins[(y, x)] = totalBasins
            totalBasins += 1

#print(suml)

print(basins)

finished = False

while not finished:
    pass