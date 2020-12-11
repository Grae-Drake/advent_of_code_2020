with open('data/problem_1.txt') as file:
    text = file.readlines()
    data = set([int(x) for x in text])
    for x in data:
        for y in data:
            if 2020 - x - y in data:
                print(x * y * (2020 - x - y))
