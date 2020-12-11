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
    return passports


def validate(passport):
    required_fields = [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = True
    for field in required_fields:
        if field not in passport:
            print("Field {} not in passport {}".format(field, passport))
            valid = False
    return valid


passports = load('data/problem_7.txt')
validated = [validate(passport) for passport in passports]
print(len(filter(lambda x: x, validated)))
        