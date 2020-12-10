data = open('day2.txt','r')
lines =  data.read().splitlines()

count = 0
for line in lines:
    a,b,c = line.split(' ')
    
    (low, high) =(int(x) for x in a.split('-'))
    letter = b[0]
    password = c

    if password.count(letter)>high or password.count(letter) < low:
        count += 1

print('part1:', len(lines)-count)

count = 0
for line in lines:
    a,b,c = line.split(' ')
    
    (p1, p2) =(int(x)-1 for x in a.split('-'))
    letter = b[0]
    password = c

    if (password[p1] == letter or password[p2] == letter):
        if not (password[p1] == letter and password[p2] == letter):
            count += 1
print('part2:', count)


