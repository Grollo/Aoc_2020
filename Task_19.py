import re

input = open('input', 'r').readlines()
input = [n.strip() for n in input]

maxdepth = 15

def gensubregex(line, regexes, result):
    if ' ' in line:
        parts = line.split(' ')
        regexes = genregexes(lines, parts[0], regexes)
        regexes = genregexes(lines, parts[1], regexes)
        result = regexes[parts[0]] + regexes[parts[1]]
    else:
        regexes = genregexes(lines, line, regexes)
        result = regexes[line]
    return result, regexes

def genregexes(lines, rulenumber, regexes):
    if rulenumber in  regexes:
        return regexes
    elif '"' in lines[rulenumber]:
        regexes[rulenumber] = lines[rulenumber][1:-1]
        return regexes
    else:
        result = ''
        if lines[rulenumber] == 'loop':
            regexes = genregexes(lines, '42', regexes)
            if rulenumber == '8':
                result = regexes['42'] + '+'
            else:
                regexes = genregexes(lines, '31', regexes)
                runningtotal = regexes['42'] + regexes['31']
                result = runningtotal
                for _ in range(1, maxdepth):
                    runningtotal = regexes['42'] + runningtotal + regexes['31']
                    result += '|'  + runningtotal
                result = '(' + result + ')'
        else:
            if '|' in lines[rulenumber]:
                orwise = lines[rulenumber].split(' | ')
                result1, regexes = gensubregex(orwise[0], regexes, result)
                result2, regexes = gensubregex(orwise[1], regexes, result)
                result = '(' + result1 + '|' + result2 + ')'
            else:
                result, regexes = gensubregex(lines[rulenumber], regexes, result)

        regexes[rulenumber] = result
        return regexes


lines = dict()
messages = []
for line in input:
    if ':' in line:
        parts = line.split(': ')
        lines[parts[0]] = parts[1]
    elif line != '':
        messages.append(line)

regexes = genregexes(lines, '0', dict())
rulezero = '^' + regexes['0'] + '$'

sum = 0
for message in messages:
    if re.match(rulezero, message):
        sum += 1
print(sum)

lines['8'] = 'loop'
lines['11'] = 'loop'

regexes = genregexes(lines, '0', dict())
rulezero = '^' + regexes['0'] + '$'

sum = 0
for message in messages:
    if re.match(rulezero, message):
        sum += 1
print(sum)
