
input = open('input', 'r').readlines()
input = [n.strip() for n in input]

row = 0
column = 0

allseats = []

for line in input:
    if line != "":
        for i in range(7):
            if line[i] == 'B':
                row += 2**(6-i)
        for i in range(3):
            if line[i+7] == 'R':
                column += 2**(2-i)
        currentseat = (row * 8) + column
        row = 0
        column = 0
        allseats.append(currentseat)

allseats.sort()
previous = -10

for current in allseats:
    if previous + 2 == current:
        print(previous+1)
    previous = current
