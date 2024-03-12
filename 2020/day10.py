data = open('day10.txt','r')
joltages = [int(x) for x in data.read().splitlines()]
joltages.sort()

outlet = joltages[0] - 1
device = joltages[-1] + 3

cache = dict(zip(joltages,[-1]*len(joltages)))

def count_poss(device,joltages, outlet):
	count = 0
	if (outlet + 3) == device:
		return 1
	else:
		if outlet + 1 in joltages:
			if cache[outlet + 1] == -1:
				cache[outlet + 1] = count_poss(device, joltages, outlet+1)
			count += cache[outlet + 1]
		if outlet + 2 in joltages:
			if cache[outlet + 2] == -1:
				cache[outlet + 2] = count_poss(device, joltages, outlet+2)
			count += cache[outlet + 2]
		if outlet + 3 in joltages:
			if cache[outlet + 3] == -1:
				cache[outlet + 3] = count_poss(device, joltages, outlet+3)
			count += cache[outlet + 3]
	return count

print(count_poss(device,joltages, outlet))

