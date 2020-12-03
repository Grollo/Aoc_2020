input = open("input", "r").readlines()
input = [n.strip() for n in input]
width = len(input[0])
x1 = 0
x3 = 0
x5 = 0
x7 = 0
xhalf = 0
trees1 = 0
trees3 = 0
trees5 = 0
trees7 = 0
treeshalf = 0
odd = False

for y in range(1,len(input)):
    x1 = (x1 + 1) % width
    if input[y][x1] == "#":
        trees1 = trees1 + 1

    x3 = (x3 + 3) % width
    if input[y][x3] == "#":
        trees3 = trees3 + 1

    x5 = (x5 + 5) % width
    if input[y][x5] == "#":
        trees5 = trees5 + 1

    x7 = (x7 + 7) % width
    if input[y][x7] == "#":
        trees7 = trees7 + 1

    if odd:
        xhalf = (xhalf + 1) % width
        if input[y][xhalf] == "#":
            treeshalf = treeshalf + 1
    odd = not odd

print(trees1)
print(trees3)
print(trees5)
print(trees7)
print(treeshalf)
print(trees1 * trees3 * trees5 * trees7 * treeshalf)
