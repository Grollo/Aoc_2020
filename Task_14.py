input = open('input', 'r').readlines()
input = [n.strip() for n in input]

def submasks(total, xmask):
    if len(xmask) == 1:
        return [total, total + xmask[0]]
    return submasks(total, xmask[1:]) + submasks(total + xmask[0], xmask[1:])

allones = (2 ** 36) - 1
maskzeroes = allones
maskones = 0
maskxes = []
allsubmasks = []
memory = dict()
secondmemory = dict()
for line in input:
    instructions = line.split(' = ')
    type = instructions[0]
    value = instructions[1]
    if type == 'mask':
        maskzeroes = allones
        maskones = 0
        maskxes = []
        allsubmasks = []
        for i in range(len(value)):
            if value[i] == '0':
                maskzeroes -= 2 ** (35-i)
            elif value[i] == '1':
                maskones += 2 ** (35-i)
            else:
                maskxes.append(2 ** (35-i))
        allsubmasks = submasks(0, maskxes)
    else:
        address = int(type[4:-1])
        maskedvalue = (int(value) | maskones) & maskzeroes
        memory[address] = maskedvalue
        maskedaddress = address | maskones
        floatingaddresses = []
        fullxmask = max(allsubmasks)
        for floatingmask in allsubmasks:
            secondmemory[(maskedaddress & (allones - fullxmask)) | floatingmask] = int(value)

sum = 0
for key in memory:
    sum += memory[key]
print(sum)
sum = 0
for key in secondmemory:
    sum += secondmemory[key]
print(sum)
