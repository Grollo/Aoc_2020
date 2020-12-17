input = open('input', 'r').readlines()
input = [n.strip() for n in input]

steps = 6
inputsize = len(input)

def pad(hyperspacetopad):
    for x in range(0, len(hyperspacetopad)):
        for y in range(0, len(hyperspacetopad[x])):
            for z in range(0, len(hyperspacetopad[x][y])):
                hyperspacetopad[x][y][z].insert(0, 0)
                hyperspacetopad[x][y][z].append(0)
            firstline = [0] * len(hyperspacetopad[0][0][0])
            lastline = [0] * len(hyperspacetopad[0][0][0])
            hyperspacetopad[x][y].insert(0, firstline)
            hyperspacetopad[x][y].append(lastline)
        firstplane = [[0] * len(hyperspacetopad[0][0][0])] * len(hyperspacetopad[0][0])
        lastplane = [[0] * len(hyperspacetopad[0][0][0])] * len(hyperspacetopad[0][0])
        hyperspacetopad[x].insert(0, firstplane)
        hyperspacetopad[x].append(lastplane)
    firstspace = [[[0] * len(hyperspacetopad[0][0][0])] * len(hyperspacetopad[0][0])] * len(hyperspacetopad[0])
    lastspace = [[[0] * len(hyperspacetopad[0][0][0])] * len(hyperspacetopad[0][0])] * len(hyperspacetopad[0])
    hyperspacetopad.insert(0, firstspace)
    hyperspacetopad.append(lastspace)

def inbounds(x, y, z, w, hyperspacetocheck):
    return x >= 0 and y >= 0 and z >= 0 and w >= 0 and x < len(hyperspacetocheck) and y < len(hyperspacetocheck[0]) and z < len(hyperspacetocheck[0][0]) and w < len(hyperspacetocheck[0][0][0])

def getnext(oldhyperspace):
    newhyperspace = []
    for x in range(0, len(oldhyperspace)):
        newspace = []
        for y in range(0, len(oldhyperspace[x])):
            newplane = []
            for z in range(0, len(oldhyperspace[x][y])):
                newline = []
                for w in range(0, len(oldhyperspace[x][y][z])):
                    activeneighbours = 0
                    for xa in range(x-1, x+2):
                        for ya in range(y-1, y+2):
                            for za in range(z-1, z+2):
                                for wa in range(w-1, w+2):
                                    if inbounds(xa, ya, za, wa, oldhyperspace) and not (x == xa and y == ya and z == za and w == wa):
                                        activeneighbours += oldhyperspace[xa][ya][za][wa]
                    if (oldhyperspace[x][y][z][w] == 1 and (activeneighbours == 2 or activeneighbours == 3)) or (oldhyperspace[x][y][z][w] == 0 and activeneighbours == 3):
                        newline.append(1)
                    else:
                        newline.append(0)
                newplane.append(newline)
            newspace.append(newplane)
        newhyperspace.append(newspace)
    return newhyperspace

hyperspace = []
space = []
plane = []
space.append(plane)
hyperspace.append(space)
for text in input:
    line = []
    for point in text:
        if point == '#':
            line.append(1)
        else:
            line.append(0)
    plane.append(line)

for i in range(steps):
    pad(hyperspace)
    hyperspace = getnext(hyperspace)

total = 0
for x in range(0, len(hyperspace)):
    for y in range(0, len(hyperspace[0])):
        for z in range(0, len(hyperspace[0][0])):
            total += sum(hyperspace[x][y][z])

print(total)
