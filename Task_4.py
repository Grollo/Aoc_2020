import re

input = open('input', 'r').readlines()
input = [n.strip() for n in input]
requiredfields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

requirements = {
    'byr': '^19[2-9][0-9]$|^200[0-2]$',
    'iyr': '^201[0-9]$|^2020$',
    'eyr': '^202[0-9]$|^2030$',
    'hgt': '^1[5-8][0-9]cm$|^19[0-3]cm$|^59in$|^6[0-9]in$|^7[0-6]in$',
    'hcl': '^#[0-9a-f]{6,6}$',
    'ecl': '^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$',
    'pid': '^[0-9]{9,9}$',
    'cid': '.*',
}

valid = 0

def validatefields(fields, invalid):
    if invalid:
        return False
    missingsome = False
    for requirement in requiredfields:
        if not requirement in fields:
            missingsome = True
    if not missingsome:
        return True

currentfields = []
invalidvalue = False
for i in range(len(input)):
    line = input[i]
    if line == '':
        if validatefields(currentfields, invalidvalue):
            valid = valid + 1
        currentfields = []
        invalidvalue = False
    else:
        for field in line.split(' '):
            fieldtype = field.split(':')[0]
            value = field.split(':')[1]
            currentfields.append(fieldtype)
            if not re.match(requirements[fieldtype], value):
                invalidvalue = True
if validatefields(currentfields, invalidvalue):
    valid = valid + 1

print(str(valid))
