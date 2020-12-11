import re


def load(path):
    with open(path) as file:
        raw = file.readlines()
        raw = ''.join(raw)
        raw = raw.split('\n\n')
        raw = [re.split(' |\n',line) for line in raw]
        passports = []
        for raw_passport in raw:
            munged_passport = {}
            for pair in raw_passport:
                if pair:
                    key, value = pair.split(':')
                    munged_passport[key] = value
            passports.append(munged_passport)
    print("Loaded {} passports.".format(len(passports)))
    return passports

def byr (data):
    # (Birth Year) - four digits; at least 1920 and at most 2002.
    return int(data) >= 1920 and int(data) <=2002

def iyr (data):
    # (Issue Year) - four digits; at least 2010 and at most 2020.
    return int(data) >= 2010 and int(data) <=2020

def eyr (data):
    # (Expiration Year) - four digits; at least 2020 and at most 2030.
    return int(data) >= 2020 and int(data) <=2030

def hgt (data):
    # (Height) - a number followed by either cm or in:
    #   - If cm, the number must be at least 150 and at most 193.
    #   - If in, the number must be at least 59 and at most 76.
    value = int(re.sub("[^0-9]", "", data))
    metric = re.sub("[0-9]", "",data)
    if metric == "in":
        return value >= 59 and value <= 76
    elif metric == "cm":
        return value >= 150 and value <= 193
    else:
        return False

def hcl (data):
    # (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    value = re.sub("[^0-9a-f]", "", data)
    return data[0] == '#' and len(value) == 6

def ecl (data):
    # (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    return data in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

def pid (data):
    # (Passport ID) - a nine-digit number, including leading zeroes.
    return len(data) == 9 and len(re.sub("[^0-9]", "", data)) == 9


def validate_field(field, data):
    validation_functions = {
        'byr': byr,
        'iyr': iyr,
        'eyr': eyr,
        'hgt': hgt,
        'hcl': hcl,
        'ecl': ecl,
        'pid': pid
    }

    if field in validation_functions:
        return validation_functions[field](data)
    else:
        return True


def contains_required_fields(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    result = True
    for field in required_fields:
        if field not in passport:
            result = False
    return result

def validate_passport(passport):
    has_required_fields = contains_required_fields(passport)
    fields_are_valid = True
    for field, value in passport.items():
        if not validate_field(field, value):
            fields_are_valid = False
    # print(passport)
    # print("Has required fields: {}".format(has_required_fields))
    # print("Fields are valid: {}".format(fields_are_valid))
    # print('')
    return has_required_fields and fields_are_valid


passports = load('data/problem_7.txt')
validated = [validate_passport(passport) for passport in passports]
print(len(filter(lambda x: x, validated)))
        