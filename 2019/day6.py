def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    orbits = fileObj.read().split('\n') #puts the file into an array
    orbits = [tuple(orbit.split(')')) for orbit in orbits]
    fileObj.close()
    return orbits


path = '/day6.txt'
orbits = readFile(path)

#had to take help on this one, cred: topaz
planets = set()
for a,b in orbits:
    planets.add(a)
    planets.add(b)
    
def countorbits(planet):
    count = 0
    sat = planet
    while sat:
        sat = list(filter(lambda x: x[1] == sat, orbits))
        if sat:
            sat = sat[0][0]
            count += 1
    return count

totalorbits = sum([countorbits(planet) for planet in planets])
print(totalorbits)


def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    orbits = fileObj.read().split('\n') #puts the file into an array
    orbits = [tuple(orbit.split(')')) for orbit in orbits]
    fileObj.close()
    return orbits


path = r'E:\projects\aoc\input\d6.txt'
orbits = readFile(path)

def orbitlist(planet):
    allorbits = []
    sat = planet
    while sat:
        sat = list(filter(lambda x: x[1] == sat, orbits))
        if sat:
            sat = sat[0][0]
            allorbits.append(sat)
    return allorbits

def mintransfer(src, dst): 
    for planet in src:
        if planet in dst:
            return src.index(planet) + dst.index(planet)
    return None

ntransfer = mintransfer(orbitlist('YOU'),orbitlist('SAN'))
print(ntransfer)