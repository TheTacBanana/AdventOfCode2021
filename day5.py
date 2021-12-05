def CalcLinePoints(p1, p2):
    if p1[0] == p2[0]:
        if p2[1] - p1[1] < 0: return [[p1[0], p1[1] + i] for i in range(0, p2[1] - p1[1] - 1, -1)]
        else: return [[p1[0], p1[1] + i] for i in range(0, p2[1] - p1[1] + 1)]

    elif p1[1] == p2[1]:
        if p2[0] - p1[0] < 0: return [[p1[0] + i, p1[1]] for i in range(0, p2[0] - p1[0] - 1, -1)]
        else: return [[p1[0] +  i, p1[1]] for i in range(0, p2[0] - p1[0] + 1)]

    return None

def CalcDiagonalPoint(p1, p2):
    dif1 = p2[0] - p1[0]
    dif2 = p2[1] - p1[1]
    if dif1 == dif2:
        if p2[1] - p1[1] < 0: return [[p1[0] + i, p1[1] + i] for i in range(0, p2[1] - p1[1] - 1, -1)]
        else: return [[p1[0] + i, p1[1] + i] for i in range(0, p2[1] - p1[1] + 1)]
    
    elif dif1 == -dif2:
        if p2[1] - p1[1] < 0: return [[p1[0] - i, p1[1] + i] for i in range(0, p2[1] - p1[1] - 1, -1)]
        else: return [[p1[0] - i, p1[1] + i] for i in range(0, p2[1] - p1[1] + 1)]

    return None

with open("input.txt") as f:
    lines = f.readlines()

lines = [lines[i].strip().split(" -> ") for i in range(len(lines))]


width = 1500
vents = [[0 for i in range(width)] for j in range(width)]

for line in lines:
    p1 = line[0].split(",")
    p1[0] = int(p1[0])
    p1[1] = int(p1[1])
    p2 = line[1].split(",")
    p2[0] = int(p2[0])
    p2[1] = int(p2[1])
    
    points = CalcLinePoints(p1, p2)

    if points != None:
        for point in points:
            vents[point[1]][point[0]] += 1

    points = CalcDiagonalPoint(p1, p2)

    if points != None:
        for point in points:
            vents[point[1]][point[0]] += 1

total = 0
for vent in vents:
    temp = ""
    for i in range(len(vent)):
        if vent[i] == 0: temp += "."
        else: temp += str(vent[i])

        if vent[i] >= 2:
            total += 1
    #print(temp)
print(total)
