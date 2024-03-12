import numpy as np

data = open('day3.txt','r')
forest = data.read().splitlines()
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

def tree_counter(forest,right, down):
    row = 0
    col = 0
    tree = 0
    while row < len(forest):
        if col >= len(forest[row]):
            col = col - len(forest[row])

        if forest[row][col] == '#':
            tree += 1

        row += down
        col += right
    return tree
prod = 1
for slope in slopes:
    right,down = slope
    print('right:', right, 'down:', down, '--', tree_counter(forest,right, down))
    prod *= tree_counter(forest, right, down)
print('-'*30)
print('product is', prod)

