with open('data/problem_1.txt') as file:
    text = file.readlines()
    data = set([int(x) for x in text])
    for x in data:
        if 2020 - x in data:
            print(x * (2020 - x))
