def Eval(bytes):
    if len(bytes) < 6:
        return 0, 0
    version = int(bytes[0:3], 2)
    typeid = int(bytes[3:6], 2)
    pos = 6
    if typeid == 4:
        lastdigit = False
        literal = ""
        while not lastdigit:
            digits = bytes[pos : pos + 5]
            lastdigit = digits[0] == "0"
            literal += digits[1:5]
            pos += 5
    else:
        optype = bytes[pos]
        pos += 1

        if optype == "0":
            length = int(bytes [pos : pos + 15], 2)
            pos += 15
            newpos = 0
            while newpos < length:
                newversion, prog = Eval(bytes [pos + newpos : pos + length])
                version += newversion
                newpos += prog
            pos += length
        else:
            packetcount = int(bytes[pos : pos + 11], 2)
            pos += 11
            for i in range(packetcount):
                newversion, length = Eval(bytes[pos:])
                version += newversion
                pos += length

    return version, pos

def Eval2(b):
    if len(b) < 6:
        return 0, 0
    version = int(b[0:3], 2)
    typeid = int(b[3:6], 2)
    pos = 6
    if typeid == 4:
        lastdigit = False
        literal = ""
        while not lastdigit:
            digit_s = b[pos : pos + 5]
            lastdigit = digit_s[0] == "0"
            literal += digit_s[1:5]
            pos += 5
        result = int(literal, 2)
    else:
        optype = b[pos]
        pos += 1

        vals = []
        if optype == "0":
            length = int(b[pos : pos + 15], 2)
            pos += 15
            newpos = 0
            while newpos < length:
                newval, prog = Eval2(b[pos + newpos : pos + length])
                vals.append(newval)
                newpos += prog
            pos += length
        else:
            num_subpackets = int(b[pos : pos + 11], 2)
            pos += 11
            for i in range(num_subpackets):
                newval, prog = Eval2(b[pos:])
                vals.append(newval)
                pos += prog

        if typeid == 0: 
            result = sum(vals)
        elif typeid == 1: 
            result = 1
            for v in vals:
                result *= v
        elif typeid == 2:
            result = min(vals)
        elif typeid == 3:
            result = max(vals)
        elif typeid == 5: 
            if vals[0] > vals[1]:
                result = 1
            else:
                result = 0
        elif typeid == 6: 
            if vals[0] < vals[1]:
                result = 1
            else:
                result = 0
        elif typeid == 7: 
            if vals[0] == vals[1]:
                result = 1
            else:
                result = 0

    return result, pos

with open("input.txt") as f:
    line = f.read().strip()

b = f"{int(line,16):0{4 * len(line)}b}"
print(Eval(b)[0], Eval2(b)[0])