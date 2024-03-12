file = open("./day2.txt")
text = file.read()
break_ids = []
limits = {
    'red':12,'green':13, 'blue':14
}
def check_sets(sets, limits):
    for set_ in sets:
            balls = set_.split(', ')
            for ball in balls:
                info = ball.split(' ')
                num, color = info[-2], info[-1]
                if int(num) > limits[color]:
                    return False
    return True

def product(lst):
    prod = 1
    for num in lst:
        prod *= num
    return prod


def power(sets):
    max_num = {'red':0,'blue':0,'green':0}
    for set_ in sets:
            balls = set_.split(', ')
            for ball in balls:
                info = ball.split(' ')
                num, color = info[-2], info[-1]
                if int(num)>max_num[color]:
                    max_num[color] = int(num)
                    
    return product(list(max_num.values()))

total_power = 0
for line in text.splitlines():
    name,sets = line.split(':')
    _,game_id = name.split(' ')
    sets = sets.split('; ')
    if check_sets(sets, limits):
        break_ids.append(int(game_id))
    total_power += power(sets)

print(sum(break_ids))
print(total_power)