from collections import Counter

with open("input.txt") as f:
    lines = [i.strip() for i in f.readlines()]

template = lines[0]
curpolymer = template

lines = [i.split(" -> ") for i in lines[2:]]

newpolymer = ""
for i in range(40):
    print(i)
    newpolymer = ""
    for c in range(1, len(curpolymer)):
        flag = False
        for m in range(len(lines)):
            if curpolymer[c - 1] + curpolymer[c] == lines[m][0]:
                newpolymer += curpolymer[c - 1] + lines[m][1]
                break
    newpolymer += curpolymer[c]
    
    curpolymer = newpolymer

counts = Counter(curpolymer)
maxc = max(counts, key = counts.get) 
minc = min(counts, key = counts.get)

print(curpolymer.count(maxc) - curpolymer.count(minc))




