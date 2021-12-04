class Table:
    def __init__(self, tableLines):
        self.tableLines = tableLines
        self.boolTable = [[False for i in range(5)] for j in range(5)]

    def CheckBoolTable(self):
        for i in range(len(self.boolTable)):
            if sum(self.boolTable[i]) == 5:
                return True
        
        for i in range(len(self.boolTable)):
            listSum = []
            for j in range(len(self.boolTable)):
                listSum.append(self.boolTable[j][i])

            if sum(listSum) == 5:
                return True

        return False

    def SumUnmarked(self):
        total = 0
        for i in range(len(self.boolTable)):
            total += sum([int(self.tableLines[i][j]) for j in range(5) if self.boolTable[i][j] == False])
        return total

    def CheckTable(self, numList):
        for i in range(len(numList)):
            for row in range(len(self.tableLines)):
                for col in range(len(self.tableLines)):
                    if int(self.tableLines[row][col]) == int(numList[i]):
                        self.boolTable[row][col] = True
                        if self.CheckBoolTable():
                            return i
                        
def MakeTables(inputLines):
    tableList = []
    temp2dlist = []
    for line in inputLines:
        if line == "\n" and temp2dlist != []:
            tableList.append(Table(temp2dlist))
            temp2dlist = []
        elif line != "\n":
            temp = line.strip().split(" ")
            temp2dlist.append([temp[i] for i in range(len(temp)) if temp[i] != ""])
    return tableList

with open("input.txt") as f:
    lines = f.readlines()

bingoNumbers = lines[0].split(",")

inputLines = lines[1:-1]

tableList = MakeTables(inputLines)

results = [tableList[i].CheckTable(bingoNumbers) for i in range(len(tableList))]

minn = min(range(len(results)), key=results.__getitem__)
maxx = max(range(len(results)), key=results.__getitem__)

print(tableList[minn].SumUnmarked(), bingoNumbers[results[minn]])
print(int(tableList[minn].SumUnmarked())* int(bingoNumbers[results[minn]]))
print()
print(tableList[maxx].SumUnmarked(), bingoNumbers[results[maxx]])
print(int(tableList[maxx].SumUnmarked())* int(bingoNumbers[results[maxx]]))