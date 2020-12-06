input = open('input', 'r').readlines()
input = [n.strip() for n in input]

totalany = 0
totalall = 0
currentmap = { }
members = 0

for line in input:
    if line == '':
        totalany += len(currentmap)
        for question in currentmap:
            if currentmap[question] == members:
                totalall += 1
        currentmap = { }
        members = 0
    else:
        members += 1
        for question in line:
            if question in currentmap:
                currentmap[question] = currentmap[question] + 1
            else:
                currentmap[question] = 1


totalany += len(currentmap)
for question in currentmap:
    if currentmap[question] == members:
        totalall += 1

print(totalany)
print(totalall)
