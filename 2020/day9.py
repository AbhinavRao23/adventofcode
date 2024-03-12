data = open('day9.txt','r')
numbers  = [int(number) for number in data.read().splitlines()]

#preamble
pmbl = 25
found = 0
for i in range(25,len(numbers)):
    for number in numbers[i-25:i]:
        if (((numbers[i]-number) not in numbers[i-25:]) and ((numbers[i] - number)  != number)):
            print(numbers[i])
            found = 1
            break
        else:
            pass
    if found == 1:
        break
