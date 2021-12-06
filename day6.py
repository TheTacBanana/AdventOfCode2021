def cycle(lfish):
    for key in lfish:
        if key != "-1":
            #print(lfish)
            #print(key, str(int(key) - 1))
            lfish[str(int(key) - 1)] = lfish[key]
            lfish[key] = 0
            #print(lfish)

        
    lfish["6"] += lfish["-1"]
    lfish["8"] += lfish["-1"]
    print("added ", lfish["-1"])
    lfish["-1"] = 0

    return lfish


with open("input.txt") as f:
    lanternfish = f.read().split(",")

print(lanternfish)

fishDict = {"-1":0,"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0}

for fish in lanternfish:
    fishDict[str(fish)] += 1

for i in range(256):
    fishDict = cycle(fishDict)
    #print(fishDict)

sumd = 0
for key in fishDict:
    sumd += fishDict[key]

print(sumd)