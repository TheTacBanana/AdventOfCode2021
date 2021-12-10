def brackettest(strIn):
    stack = []
    illegal = {")":3, "]":57, "}":1197, ">":25137}
 
    for c in strIn:
        if c in ["(", "{", "[", "<"]:
            stack.append(c)
        else:

            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if c != ")":
                    return illegal[c]
            if current_char == '{':
                if c != "}":
                    return illegal[c]
            if current_char == '[':
                if c != "]":
                    return illegal[c]
            if current_char == '<':
                if c != ">":
                    return illegal[c]

    if stack:
        return False
    return True

def completebrackets(strIn):
    stack = []
 
    notfinishedtotal = 0
    bracketPoints = {")": 1, "]": 2, "}":3, ">":4}

    for c in strIn:
        if c in ["(", "{", "[", "<"]:
            stack.append(c)
        else:
            current_char = stack.pop()
            if current_char == '(':
                if c != ")":
                    notfinishedtotal += bracketPoints[")"]
            if current_char == '{':
                if c != "}":
                    notfinishedtotal += bracketPoints["}"]
            if current_char == '[':
                if c != "]":
                    notfinishedtotal += bracketPoints["]"]
            if current_char == '<':
                if c != ">":
                    notfinishedtotal += bracketPoints[">"]

    for i in range(len(stack)):
        char = stack.pop()
        if char == '(':
            notfinishedtotal = (notfinishedtotal * 5) + bracketPoints[")"]
        if char == '{':
            notfinishedtotal = (notfinishedtotal * 5) + bracketPoints["}"]
        if char == '[':
            notfinishedtotal= (notfinishedtotal * 5) + bracketPoints["]"]
        if char == '<':
            notfinishedtotal = (notfinishedtotal * 5) + bracketPoints[">"]

    return notfinishedtotal

with open("input.txt") as f:
    lines = [i.strip() for i in f.readlines()]

newLines = []

sumIl = 0
for line in lines:
    new = brackettest(line)
    if new != False:
        sumIl += new
    else:
        newLines.append(line)

print(sumIl)

scores = []

for line in newLines:
    new = completebrackets(line)

    scores.append(new)

scores.sort()
print(scores[int((len(scores) - 1)/2)])