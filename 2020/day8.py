data = open('day8.txt','r')
instructions = data.read().splitlines()
acc = 0
i = 0
visited = []
while i not in visited:  
    visited.append(i)
    (cmd,val) = instructions[i].split(' ')
    val = int(val[1:]) if val[0]=='+' else -1* int(val[1:])
    if cmd == 'acc':
        acc += val
        i += 1
    elif cmd == 'jmp':
        i += val
    else:
        i += 1

print('part 1:', acc)

jmps = []
nops = []

for i,inst in enumerate(instructions):
    if inst[:3] == 'jmp':
        jmps.append(i)
    elif inst[:3] == 'nop':
        nops.append(i)
    else:
        pass
def accumulator(instructions): 
    i = 0
    visited = []
    acc = 0
    while i < len(instructions):  
        if i in visited:
            return 0, acc
        else:
            visited.append(i)
            (cmd,val) = instructions[i].split(' ')
            val = int(val[1:]) if val[0]=='+' else -1* int(val[1:])
            if cmd == 'acc':
                acc += val
                i += 1
            elif cmd == 'jmp':
                i += val
            else:
                i += 1
    return 1,acc
    
data = open('day8.txt','r')
instructions = data.read().splitlines()

for jmp in jmps:
    instructions_mod = instructions.copy()
    instructions_mod[jmp] = 'nop'+instructions_mod[jmp][3:]
    ended, acc = accumulator(instructions_mod)
    if ended == 1:
        print('patr 2:', acc)
for nop in nops:
    instructions_mod = instructions.copy()
    instructions_mod[jmp] = 'nop'+instructions_mod[jmp][3:]
    ended, acc = accumulator(instructions_mod)
    if ended == 1:
        print('patr 2:', acc)
