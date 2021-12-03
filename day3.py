with open("input.txt") as f:
    lines = f.readlines()

    gr = ""
    er = ""
    nums = [0 for i in range(len(lines[0]))]
    for i in range(len(lines)):
        for c in range(len(lines[i])):
            if lines[i][c] == "1":
                nums[c] += 1

    for c in range(len(lines[i])):
        if nums[c] > len(lines) / 2:
            gr += "1"
            er += "0"
        else:
            gr += "0"
            er += "1"

    print(int(gr,2)*int(er,2))

    og = ""
    co2 = ""

    curList = lines
    for c in range(len(curList[i].strip())):
        onelist = []
        zerolist = []
        for i in range(len(curList)):
            if curList[i][c].strip() == "1":
                onelist.append(curList[i].strip())
            else:
                zerolist.append(curList[i].strip())

        if len(onelist) == len(zerolist):
            curList = onelist
        elif len(onelist) > len(zerolist):
            curList = onelist
        else:
            curList = zerolist
    og = curList

    curList = lines
    for c in range(len(curList[i].strip())):
        onelist = []
        zerolist = []
        for i in range(len(curList)):
            if curList[i][c].strip() == "1":
                onelist.append(curList[i].strip())
            else:
                zerolist.append(curList[i].strip())

        if len(curList) == 1:
            break
        if len(onelist) == len(zerolist):
            curList = zerolist
        elif len(onelist) < len(zerolist):
            curList = onelist
        else:
            curList = zerolist
    co2 = curList

    print(int(og[0], 2)*int(co2[0], 2))
    