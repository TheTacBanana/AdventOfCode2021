class Display:
    def __init__(self, inputData):
        self.inputData = inputData.split(" | ")
        self.segments = self.inputData[0].split(" ")
        self.displayOut = self.inputData[1].split(" ")

        self.fivers = []
        self.fiversets = None
        self.sixers = []
        self.sixersets = None

        self.numSets = [None for i in range(10)]
        self.segmentData = {"t":"","tl":"","tr":"","m":"","bl":"","br":"","b":""}

    def CalculatePart1(self):
        total = 0
        for out in self.displayOut:
            if len(out) in [2, 4, 3, 7]:
                total += 1
        return total

    def CalculatePart2(self):
        for segs in self.segments:
            #print(segs)
            lo = len(segs)
            if lo == 5:
                self.fivers.append(set(segs))
            if lo == 6:
                self.sixers.append(set(segs))

            if lo == 2: self.numSets[1] = set(segs)
            elif lo == 4: self.numSets[4] = set(segs)
            elif lo == 3: self.numSets[7] = set(segs)
            elif lo == 7: self.numSets[8] = set(segs)

        # Fivers
        self.fiversets = set(self.fivers[0]).intersection(set(self.fivers[1]), set(self.fivers[2]))
        print(self.fiversets)

        # Sixers
        self.sixersets = set(self.sixers[0]).intersection(set(self.sixers[1]), set(self.sixers[2]))
        print(self.sixersets)

        # Logic

        # t
        self.segmentData["t"] = list(self.numSets[7] - self.numSets[1])[0]

        # bl & b
        bandbl = (self.numSets[8] - self.numSets[7]) - self.numSets[4]  
        empty = set()
        for six in self.sixers:
            new = bandbl - six
            if new != empty:
                self.segmentData["bl"] = list(new)[0]
                self.segmentData["b"] = list(bandbl - new)[0]
                break
        
        # m & tl
        m = (self.fiversets - set(self.segmentData["t"])) - set(self.segmentData["b"])
        self.segmentData["m"] = list(m)[0]

        fourminus7 = self.numSets[4] - self.numSets[7]
        tl = fourminus7 - m
        self.segmentData["tl"] = list(tl)[0]

        # br
        br = self.sixersets - set(self.segmentData["tl"]) - set(self.segmentData["t"]) - set(self.segmentData["b"])
        self.segmentData["br"] = list(br)[0]

        # tr
        l = ""
        for key in self.segmentData:
            l += self.segmentData[key]

        s = set(l)
        tr = self.numSets[8] - s
        self.segmentData["tr"] = list(tr)[0]

    def CalcValue(self):
        valstr = ""
        for out in self.displayOut:
            valstr += str(self.ConvertSegmentToNum(out))
        print(int(valstr))
        return int(valstr)

    def ConvertSegmentToNum(self, segment):
        # 0
        segmentset = set(segment)
        
        if segmentset == self.numSets[1]:
            return 1
        elif self.numSets[8] - segmentset == set(self.segmentData["tl"] + self.segmentData["br"]):
            return 2
        elif self.numSets[8] - segmentset == set(self.segmentData["tl"] + self.segmentData["bl"]):
            return 3
        elif segmentset == self.numSets[4]:
            return 4
        elif self.numSets[8] - segmentset == set(self.segmentData["tr"] + self.segmentData["bl"]):
            return 5
        elif self.numSets[8] - segmentset == set(self.segmentData["tr"]):
            return 6
        elif segmentset == self.numSets[7]:
            return 7
        elif segmentset == self.numSets[8]:
            return 8
        elif self.numSets[8] - segmentset == set(self.segmentData["bl"]):
            return 9 
        elif segmentset == segmentset - set(self.segmentData["m"]):
            return 0

with open("input.txt") as f:
    displays = f.readlines()
displays = [displays[i].strip() for i in range(len(displays))]

displayClass = []

for display in displays:
    displayClass.append(Display(display))

total = 0
total2 = 0
for display in displayClass:
    total += display.CalculatePart1()
    display.CalculatePart2()

    total2 += display.CalcValue()

print(total, total2)