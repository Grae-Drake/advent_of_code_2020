with open('data/problem_3.txt') as file:
    text = file.readlines()
    parsed = []
    for line in text:
        line = line.replace(':', '').split(' ')
        line[0] = [int(x) for x in line[0].split('-')]
        parsed.append(line)
    
    result = 0
    for password in parsed:
        positions, char, pass_string = password
        match_count = 0
        for position in positions:
            if pass_string[position - 1] == char:
                match_count += 1
        if match_count == 1:
            result += 1
    
    print(result)


