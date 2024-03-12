def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    words = fileObj.read().split(',') #puts the file into an array
    fileObj.close()
    numbers = [int(i) for i in words]
    return numbers



def intcomputer(inp, phases):   
    prevoutput = False
    for phase in phases:
        i = 0
        k = 0
        opcode = inp[0]
        while opcode != 99:
            instruction = [int(char) for char in str(inp[i])]
            
            while len(instruction)<5:
                instruction.insert(0,0)

            a,b,c,d,e = instruction
            opcode = 10*d+e
            if opcode == 99:
                break

            #setting parameters based on their respective modes
            i1 = (i+1 if c==1 else inp[i+1])
            if i+2<len(inp):
                i2 = (i+2 if b==1 else inp[i+2])
            if i+3<len(inp):    
                i3 = (i+3 if a==1 else inp[i+3])

            if opcode == 1:
                inp[i3] = inp[i1] + inp[i2]
                i = i + 4

            elif opcode == 2:
                inp[i3] = inp[i1] * inp[i2]
                i = i + 4

            elif opcode == 3:
                if k %2 == 0:
                    inp[i1] = phase
                else:
                    inp[i1] = prevoutput if prevoutput else 0
                k += 1
                i += 2

            elif opcode == 4:
                prevoutput = inp[i1]
                i += 2

            elif opcode == 5:
                i = inp[i2] if inp[i1] != 0 else i+3

            elif opcode == 6:
                i = inp[i2] if inp[i1] == 0 else i+3

            elif opcode == 7:
                inp[i3] = 1 if inp[i1] < inp[i2] else 0
                i = i + 4

            elif opcode == 8:
                inp[i3] = 1 if inp[i1] == inp[i2] else 0
                i = i + 4

            else:
                print("identifier error")
                break
    return prevoutput

path = './day7.txt' 
inputdata = readFile(path)

from itertools import permutations
phaselist = [p for p in permutations([0,1,2,3,4])]

output = []
for phases in phaselist:
    output.append(intcomputer(inputdata, phases))
print(max(output))