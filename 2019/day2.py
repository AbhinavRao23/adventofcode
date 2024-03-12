def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().split(',') #puts the file into an array
        fileObj.close()
        numbers = [int(i) for i in words]
        return numbers
    
path = "./day2.txt"
opcode = readFile(path)

opcode[1] = 12
opcode[2] = 2


def intcomputer(opcode):
    i = 0
    while opcode[i] != 99:
        if opcode[i] == 1:
            opcode[opcode[i+3]] = opcode[opcode[i+1]] + opcode[opcode[i+2]]
            i = i + 4
            continue
        elif opcode[i] ==2:
            opcode[opcode[i+3]] = opcode[opcode[i+1]] * opcode[opcode[i+2]]
            i = i + 4
            continue
        else:
            print("identifier error")
            break
    return opcode
    
print(intcomputer(opcode)[0])

opcodes = readFile(path)

for i in range(100):
    for j in range(100):
        inp = opcodes.copy()
        inp[1] = i
        inp[2] = j
        if intcomputer(inp)[0] == 19690720:
            print(i,j)
            break
        else:
            pass