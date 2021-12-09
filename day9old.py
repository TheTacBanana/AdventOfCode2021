with open("input.txt") as f:
    grid = f.readlines()
grid = [grid[i].strip() for i in range(len(grid))]
grid = [[int(grid[i][j]) for j in range(len(grid[i]))] for i in range(len(grid))]

for g in grid:
    print(g)

points = []
for row in range(len(grid)):
    for col in range(len(grid[row])):
        finished = False
        pointer = [row,col]
        #print("Start", pointer)
        while not finished:
            #print("Pointer", pointer, grid[pointer[0]][pointer[1]])
            pointVal = grid[pointer[0]][pointer[1]]

            lowestpoint = [pointer, pointVal]

            if pointer[0] != 0:
                if pointVal > grid[pointer[0] - 1][pointer[1]]:
                    if lowestpoint[1] > grid[pointer[0] - 1][pointer[1]]:
                        lowestpoint[0] = [pointer[0] - 1, pointer[1]]
                        lowestpoint[1] = grid[pointer[0] - 1][pointer[1]]
                    
            if pointer[0] != len(grid) - 1:
                if pointVal > grid[pointer[0] + 1][pointer[1]]:
                    if lowestpoint[1] > grid[pointer[0] + 1][pointer[1]]:
                        lowestpoint[0] = [pointer[0] + 1, pointer[1]]
                        lowestpoint[1] = grid[pointer[0] + 1][pointer[1]]
                    
            if pointer[1] != len(grid[0]) - 1:
                if pointVal > grid[pointer[0]][pointer[1] + 1]:
                    if lowestpoint[1] > grid[pointer[0]][pointer[1] + 1]:
                        lowestpoint[0] = [pointer[0], pointer[1] + 1]
                        lowestpoint[1] = grid[pointer[0]][pointer[1] + 1]
                    
            if pointer[1] != 0:
                if pointVal > grid[pointer[0]][pointer[1] - 1]:
                    if lowestpoint[1] > grid[pointer[0]][pointer[1] - 1]:
                        lowestpoint[0] = [pointer[0], pointer[1] - 1]
                        lowestpoint[1] = grid[pointer[0]][pointer[1] - 1]

            #print(lowestpoint[0])
            if pointer == lowestpoint[0]:
                finished = True
                if pointer not in points:
                    points.append(pointer)
            else:
                pointer = lowestpoint[0]

sumr = 0
for point in points:
    print(point, grid[point[0]][point[1]])
    sumr += grid[point[0]][point[1]] + 1

print(sumr, len(points))