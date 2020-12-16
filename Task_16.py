input = open('input', 'r').readlines()
input = [n.strip() for n in input]

linenumber = 0
line = input[linenumber]
rules = []
fieldnames = []
while line != '':
    firstsplit = line.split(': ')
    name = firstsplit[0]
    fieldnames.append(name)
    values = firstsplit[1].split(' or ')
    interval1 = values[0].split('-')
    interval2 = values[1].split('-')
    intervals = [int(interval1[0]), int(interval1[1]), int(interval2[0]), int(interval2[1])]
    rules.append(intervals)
    linenumber += 1
    line = input[linenumber]

linenumber += 2

myticket = [int(n) for n in input[linenumber].split(',')]
validtickets = [myticket]
numberoffields = len(myticket)
applicablefields = []
for i in range(numberoffields):
    newlist = []
    for j in range(numberoffields):
        newlist.append(j)
    applicablefields.append(newlist)

linenumber += 3

def followsrules(field, rule):
    return (field >= rule[0] and field <= rule[1]) or (field >= rule[2] and field <= rule[3])

errorrate = 0
while linenumber < len(input):
    fields = [int(n) for n in input[linenumber].split(',')]
    linenumber += 1

    validticket = True
    for field in fields:
        breaksrules = True
        for rule in rules:
            if followsrules(field, rule):
                breaksrules = False
        if breaksrules:
            errorrate += field
            validticket = False
    
    if validticket:
        validtickets.append(fields)

print(errorrate)

for ticket in validtickets:
    for f in range(len(ticket)):
        for r in range(len(rules)):
            if r in applicablefields[f] and not followsrules(ticket[f], rules[r]):
                applicablefields[f].remove(r)

done = False
while not done:
    done = True
    for i in range(len(applicablefields)):
        if len(applicablefields[i]) == 1:
            for j in range(len(applicablefields)):
                rule = applicablefields[i][0]
                if i != j and rule in applicablefields[j]:
                    applicablefields[j].remove(rule)
        else:
            done = False

product = 1
for i in range(len(myticket)):
    if 'departure' in fieldnames[applicablefields[i][0]]:
        product *= myticket[i]

print(product)
