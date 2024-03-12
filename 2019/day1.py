import math
import numpy as np

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        numbers = [float(i) for i in lines]
        return numbers
    
path = './day1.txt'

mass = readFile(path)
fuel = [math.floor(m/3)-2 for m in mass]
print(sum(fuel))

dfuel = fuel
while sum(dfuel) > 0:
    dfuel = [math.floor(d/3)-2 for d in dfuel]
    dfuel = [0 if d < 0 else d for d in dfuel]
    fuel = [f + d for (f,d) in zip(fuel,dfuel)]
print(sum(fuel))