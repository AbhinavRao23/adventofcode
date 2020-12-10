def number_maker(code):
    number = 0
    for i,char in enumerate(code):
        mult  = 0 if (char == 'F' or char =='L') else 1
        number += 2**(len(code)-i - 1)*mult
    return number

def seat_number(seat_id):
    row_code = seat_id[:7]
    col_code = seat_id[7:]
    return number_maker(row_code), number_maker(col_code)

data = open('day5.txt','r')
bpasses = data.read().splitlines()
max_id = 0

for bpass in bpasses:
    row,col = seat_number(bpass)
    max_id = row*8 + col if ((row*8 + col)>max_id) else max_id
print('part 1:',max_id)

ids = []
for bpass in bpasses:
    row, col = seat_number(bpass)
    ids.append(row*8+col)

ids.sort()
for i,id_ in enumerate(ids):
    if ((i != len(ids)-1) and (id_+1 not in ids)):
        print('part2:',id_ + 1)
