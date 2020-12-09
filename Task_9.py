input = open('input', 'r').readlines()
input = [int(n.strip()) for n in input]

def issumofprevious25(testindex):
    for i in range(testindex-25, testindex):
        for j in range(i+1, testindex):
            if input[i] + input[j] == input[testindex]:
                return True
    return False

def getincongrous():
    for i in range(25, len(input)):
        if not issumofprevious25(i):
            return input[i]

def findcontinousterms(number, size):
    for i in range(0,len(input)-size+1):
        terms = []
        for j in range(i, i+size):
            terms.append(input[j])
        if sum(terms) == number:
            return terms
    return []

incongrous = getincongrous()
for size in range(2, len(input)):
    terms = findcontinousterms(incongrous, size)
    if len(terms) != 0:
        print(min(terms) + max(terms))
        break
