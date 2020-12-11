with open('data/problem_3.txt') as file:
    text = file.readlines()
    parsed = []
    for line in text:
        line = line.replace(':', '').split(' ')
        line[0] = [int(x) for x in line[0].split('-')]
        parsed.append(line)
    
    result = 0
    for password in parsed:
        required_count, character, pass_string = password
        character_count = pass_string.count(character)
        if character_count >= required_count[0] and character_count <= required_count[1]:
            result += 1
    
    print(result)


