with open("input.txt") as f:
    lines = f.readlines()
    
    hor, vertical = 0, 0
    
    for line in lines:
        temp = line.split(" ")
        if temp[0] == "forward":
            hor += int(temp[1])
        elif temp[0] == "up":
            vertical -= int(temp[1])
        elif temp[0] == "down":
            vertical += int(temp[1])

    print(hor, vertical, hor * vertical)

    aim, vertical, hor = 0, 0, 0

    for line in lines:
        temp = line.split(" ")
        if temp[0] == "forward":
            hor += int(temp[1])
            vertical += int(temp[1]) * aim
        elif temp[0] == "up":
            aim -= int(temp[1])
        elif temp[0] == "down":
            aim += int(temp[1])

    print(hor, vertical, hor*vertical)



            