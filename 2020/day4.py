import re
data = open('day4.txt','r')
register = data.read().split('\n\n')
actual_fields = {'byr', 'iyr', 'eyr','hgt','hcl', 'ecl','pid','cid'}
np_fields = {'byr', 'iyr', 'eyr','hgt','hcl', 'ecl','pid'}
count = 0

for passport in register:
    fields = []
    information = re.split(' |\n' ,passport)
    for field in information:
        if len(field)>3:     
            [key,value] = field.split(':')
            fields.append(key)
    fields = set(fields)
    if fields == actual_fields:
        count += 1
    elif fields == np_fields:
        count += 1
    else:
        pass
print('part 1 valid passports:', count)


def isvalid(info):
  #years#years#years 
    byr = int(info['byr'])
    iyr = int(info['iyr'])
    eyr = int(info['eyr'])
    
    if ((1920<=byr<=2002) and (2010 <= iyr <= 2020) and  (2020 <= eyr <=2030)):
        pass
    else:
        return 0


    #height
    if info['hgt'][-2:]== 'cm':
        if (150 <= int(info['hgt'][:-2]) <= 193):
            pass
        else:
            return 0

    elif info['hgt'][-2:]== 'in':
        if (59 <= int(info['hgt'][:-2]) <= 76):
            pass
        else:
            return 0 

    else:
        return 0

    #hair color
    if len(info['hcl'])==7 and info['hcl'][0] =='#':
        for char in info['hcl'][1:]:
            if ((48  <=  ord(char) <= 57) or (97 <= ord(char) <= 102 )):
                pass
            else:
                return 0
    else:
        return 0

    #eye color
    allowed = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if info['ecl'] in allowed:
        pass
    else:
        return 0 

    #passport id
    if len(info['pid']) == 9:
        for char in info['pid'][1:]:
            if (48  <=  ord(char) <= 57):
                pass
            else:
                return 0
    else:
        return 0
    return 1

count = 0
for passport in register:
    fields = []
    information  = re.split(' |\n', passport)
    for field in information:
        if len(field) > 3:
            fields.append(field.split(':'))
    
    information = dict(fields)
    
    if set(information.keys()) == actual_fields or set(information.keys())  == np_fields:
        count += isvalid(information)
    else:
        pass
 
print('part 2 valid passports:', count)
