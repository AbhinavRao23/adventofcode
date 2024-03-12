path = './day3.txt'

def readfile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        wires = fileObj.read().split('\n') #puts the file into an array
        wire1, wire2 = wires
        wire1 = wire1.split(',')
        wire2 = wire2.split(',')
        fileObj.close()
        return wire1, wire2

wire1,wire2 = readfile(path)

def wirepath(wire):
    wirepath = [(0,0)]
    for cmd in wire:
        direction = cmd[0]
        steps = int(cmd[1:])
        if direction == 'U':
            for step in range(steps):
                wirepath.append((wirepath[-1][0],wirepath[-1][1]+1))
        elif direction == 'D':
            for step in range(steps):
                wirepath.append((wirepath[-1][0],wirepath[-1][1]-1))
        elif direction == 'R':
            for step in range(steps):
                wirepath.append((wirepath[-1][0]+1,wirepath[-1][1]))
        elif direction == 'L':
            for step in range(steps):
                wirepath.append((wirepath[-1][0]-1,wirepath[-1][1]))
        else:
            print('invalid instuction')
    return wirepath

wirepath1 = wirepath(wire1)
wirepath2 = wirepath(wire2)
intersections = list(set(wirepath1).intersection(wirepath2))
distance = [abs(a)+abs(b) for (a,b) in intersections]
distance.sort()
mindistance = distance[1]
print(mindistance)

combined_steps = []
for intersection in intersections:
    combined_step = (wirepath1.index(intersection) + wirepath2.index(intersection))
    combined_steps.append(combined_step)    

combined_steps.sort()
print(combined_steps[1])