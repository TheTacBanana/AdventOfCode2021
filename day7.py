import math

with open("input.txt") as f:
    crabs = f.read().split(",")

crabs = [int(crabs[i]) for i in range(len(crabs))]
#print(crabs)

sums = []

for i in range(max(crabs)):
    print(i)
    sumc = 0
    for c in range(len(crabs)):
        if crabs[c] < i:  
            sumdif = [i for i in range(0, crabs[c] - i - 1, -1)]
        else: 
            sumdif = [i for i in range(0, crabs[c] - i  + 1)]

        sumc += abs(sum(sumdif))
    sums.append(sumc)
    #print(sums)

print(sums)
print(min(sums))