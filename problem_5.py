with open('data/problem_5.txt') as file:
    slope = file.readlines()
    slope = [row.strip() for row in slope]
    width = len(slope[0])
    trees_hit = 0
    for i, row in enumerate(slope):
        position = (i * 3) % width
        if row[position] == '#':
            trees_hit += 1
    print(trees_hit)

