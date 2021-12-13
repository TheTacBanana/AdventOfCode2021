with open("input.txt") as f:
    dots = [i.strip() for i in f.readlines()]

dotGrid = [[0 for i in range(1500)] for j in range(1500)]
foldLines = []

flip = False
for line in dots:

    if len(line) == 0:
        flip = True
        continue

    if not flip:
        d = line.split(",")
        dotGrid[int(d[1])][int(d[0])] = 1
    else:
        l = line.split("fold along ")
        l = l[1].split("=")
        l[1] = int(l[1])
        foldLines.append(l)

#for line in dotGrid:
#    print(line)

print(foldLines)

bounds = [1500, 1500]

#for row in range(bounds[1]):
#    strout = ""
#    for col in range(bounds[0]):
#        strout += str(dotGrid[row][col])
#    print(strout)

#print()

for i in range(len(foldLines)):
    fold = foldLines[i]
    if fold[0] == "x":
        for i in range(bounds[0] - fold[1]):
            for j in range(bounds[1]):
                dotGrid[j][fold[1] - i] += dotGrid[j][fold[1] + i]
                
                bounds[0] = fold[1]
    else:
        for i in range(bounds[1] - fold[1]):
            for j in range(bounds[0]):
                dotGrid[fold[1] - i][j] += dotGrid[fold[1] + i][j]
                bounds[1] = fold[1]

    print(bounds)

for row in range(bounds[1]):
    strout = ""
    for col in range(bounds[0]):
        if dotGrid[row][col] >= 1:
            strout += str(1)
        else:
            strout += str(0)
    print(strout)


count = 0
for row in range(bounds[1]):
    for col in range(bounds[0]):
        if dotGrid[row][col] >= 1:
            count += 1

print(count)


