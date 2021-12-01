with open("input.txt") as f:
    count = 0
    prev = None
    file = f.readlines()
    for line in file:
        if prev == None:
            prev = int(line.strip())
        elif int(line.strip()) > prev:
            count += 1
        prev = int(line.strip())

    print(count)

    newcount = 0
    tempsum = 0
    prevsum = None
    for i in range(len(file) - 2):
        tempsum = int(file[i].strip()) + int(file[i+1].strip()) + int(file[i+2].strip())
        if prevsum == None:
            pass
        elif tempsum > prevsum:
            print("count")
            newcount += 1

        prevsum = tempsum

    print(newcount)