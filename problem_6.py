import math


def load(path):
    with open(path) as file:
        return [row.strip() for row in file.readlines()]
        
        
def descend(hill, slope):
    width = len(hill[0])
    trees_hit = 0
    x = y = 0
    while y < len(hill):
        if hill[y][x % width] == '#':
            trees_hit += 1
        y += slope[0]
        x += slope[1]
    return trees_hit


slopes = [
    [1, 1],
    [1, 3],
    [1, 5],
    [1, 7],
    [2, 1]
]

hill = load('data/problem_5.txt')
trees_hit = [descend(hill, slope) for slope in slopes]
print("Trees hit: {}".format(trees_hit))
result = 1
for run in trees_hit:
    result *= run
print(result)