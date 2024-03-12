import numpy as np
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        lines = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        numbers = [int(i) for i in lines]
        return numbers

ex_report = readFile('day1.txt')

for i in range(len(ex_report)):
    for j in range(i+1,len(ex_report)):
        if ex_report[i] + ex_report[j] == 2020:
            print(ex_report[i]*ex_report[j])
            break

for i in range(len(ex_report)):
    for j in range(i+1,len(ex_report)):
        for k in range(j+1,len(ex_report)):
            if ex_report[i]+ex_report[j]+ex_report[k]==2020:
                print(ex_report[i]*ex_report[j]*ex_report[k])
                break

