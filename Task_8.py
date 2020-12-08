input = open('input', 'r').readlines()
input = [n.strip() for n in input]

programorder = []
acc = 0
pointer = 0

while True:
    if pointer in programorder:
        print(acc)
        break
    programorder.append(pointer)
    line = input[pointer].split(' ')
    if line[0] == 'acc':
        acc += int(line[1])
        pointer += 1
    elif line[0] == 'jmp':
        pointer += int(line[1])
    else:
        pointer += 1

def swapat(index):
    if 'nop' in input[index]:
        input[index] = input[index].replace('nop', 'jmp')
    else:
        input[index] = input[index].replace('jmp', 'nop')

def findswappedline():
    for operation in range(len(input)):
        if 'acc' in input[operation]:
            continue
        else:
            swapat(operation)
            programorder = []
            acc = 0
            pointer = 0
            hasrepeated = False
            while not hasrepeated:
                if pointer == len(input):
                    return acc
                if pointer in programorder:
                    hasrepeated = True
                    break
                programorder.append(pointer)
                line = input[pointer].split(' ')
                if line[0] == 'acc':
                    acc += int(line[1])
                    pointer += 1
                elif line[0] == 'jmp':
                    pointer += int(line[1])
                else:
                    pointer += 1
            swapat(operation)

print(findswappedline())
