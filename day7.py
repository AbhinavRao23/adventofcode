data = open('day7.txt','r')
rules = data.read().splitlines()

relation = {}
for rule in rules:
    key = rule.split(' contain ')[0][:-5]
    key = key.split(' ')[0]+key.split(' ')[1]
    values = rule.split(' contain ')[1].split(', ')
    for i,value in enumerate(values):
        values[i] = value.split(' ')[1]+value.split(' ')[2]
    relation[key] = values

#find every bag in dict which has my bag under their tree
#function - recursive: returns 1 if bag contains my bag or returns 0
# loop searches every bag in dict other than my bag and keep a count if mybag is found in those bags

def findmybag(rel,bag,mybag):
    if mybag in rel[bag]:
        return 1 
    else:
        for inbag in rel[bag]:
            if inbag == 'otherbags.':
                continue
            else:
                if findmybag(rel,inbag,mybag) == 1:
                    return 1
                else:
                    continue
        return 0 
mybag = 'shinygold'
count = 0


for bag in relation.keys():
    if bag != mybag:
        count += findmybag(relation, bag, mybag)
print('part 1:' ,count)


relation_bag = {}
relation_number =  {}
for rule in rules:
    numbers = []
    key = rule.split(' contain ')[0][:-5]
    key = key.split(' ')[0]+key.split(' ')[1]
    values = rule.split(' contain ')[1].split(', ')
    for i,value in enumerate(values):
        values[i] = value.split(' ')[1]+value.split(' ')[2]
        if value.split(' ')[0] == 'no':
            numbers.append(0)
        else:
            numbers.append(int(value.split(' ')[0]))
    relation_bag[key] = values
    relation_number[key] = numbers

def bagsinbag(rel_bag, rel_n, mybag):
    count = 0
    if rel_bag[mybag][0] == 'otherbags.':
        return 0
    else:
        for i,bag in enumerate(rel_bag[mybag]):
            count += rel_n[mybag][i] + rel_n[mybag][i]*bagsinbag(rel_bag, rel_n, bag)
    return count

print('part 2: 'bagsinbag(relation_bag, relation_number, 'shinygold'))
