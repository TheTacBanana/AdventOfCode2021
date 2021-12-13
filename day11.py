with open("input.txt") as f:
    grid = [i.strip() for i in f.readlines()]
    grid = [[int(grid[i][j]) for j in range(len(grid[i]))] for i in range(len(grid))]

DR = [-1,-1,-1,0,1,1,1,0]
DC = [-1,0,1,1,1,0,-1,-1]

flashcount = 0
step = 0
allflash = False
while (not allflash) or step < 100:
    for row in range(len(grid)):
        for col in range(len(grid)):
            grid[row][col] += 1

    flashed = True
    flash = [[0] * len(grid) for i in range(len(grid[0]))]
    while flashed:
        flashed = False
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 9 and flash[r][c] == 0:
                    flashed = True
                    flashcount += 1
                    flash[r][c] = 1
                    for rr,cc in zip(DR,DC):
                        rr = rr + r
                        cc = cc + c
                        if 0<=rr<len(grid) and 0<=cc<len(grid[0]):
                            grid[rr][cc] += 1

    allflash = True
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if flash[r][c] == 1:
                grid[r][c] = 0
            else:
                allflash = False

    if allflash:
        p2 = step+1

    step += 1
    if step == 100:
        p1 = flashcount

print(p1, p2)