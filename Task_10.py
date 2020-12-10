input = open('input', 'r').readlines()
input = [int(n.strip()) for n in input]

input.sort()
input.insert(0, 0)
input.append(input[len(input)-1]+3)

diffs = []

for i in range(len(input)-1):
    diffs.append(input[i+1] - input[i])

print(diffs.count(1) * (diffs.count(3)))

def without(connections, index):
    if index < len(connections) - 1:
        return connections[:index] + connections[index+1:]
    else:
        return connections[:index]

def getallsublists(connections):
    if len(connections) < 2:
        return [connections, []]
    allsublists = [connections]
    for index in range(len(connections)):
        missingone = without(connections, index)
        for sublist in getallsublists(missingone):
            if not sublist in allsublists:
                allsublists.append(sublist)
    return allsublists

def connects(connections):
    for index in range(len(connections)-1):
        if connections[index+1] - connections[index] > 3:
            return False
    return True

def possibilities(connections):
    if len(connections) < 3:
        return 1
    sum = 0
    first = connections[0]
    last = connections[len(connections)-1]
    middle = connections[1:len(connections)-1]
    for sublist in getallsublists(middle):
        sublist.insert(0, first)
        sublist.append(last)
        if connects(sublist):
            sum += 1
    return sum

sublist = []
product = 1
for i in range(0, len(diffs)):
    sublist.append(input[i])
    if diffs[i] == 3:
        product *= possibilities(sublist)
        sublist = [input[i]]

print(product)
