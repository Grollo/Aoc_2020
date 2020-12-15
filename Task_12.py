directions = open('input', 'r').readlines()
directions = [n.strip() for n in directions]

#for part 1
distanceeast = 0
distancenorth = 0
facing = 0 #east = 0, south = 1, west = 2, north = 3

#for part 2
waypointeast = 10 #relative to ship
waypointnorth = 1

positioneast = 0 #realtive to 0, 0
positionnorth = 0

for direction in directions:
    type = direction[0]
    amount = int(direction[1:])
    if type == 'N':
        distancenorth += amount
        waypointnorth += amount
    elif  type == 'S':
        distancenorth -= amount
        waypointnorth -= amount
    elif  type == 'E':
        distanceeast += amount
        waypointeast += amount
    elif  type == 'W':
        distanceeast -= amount
        waypointeast -= amount
    elif  type == 'R':
        turns = amount / 90
        facing = (facing + turns) % 4
        for turns in range(int(amount / 90)):
            tempnorth = -waypointeast
            waypointeast = waypointnorth
            waypointnorth = tempnorth
    elif  type == 'L':
        turns = amount / 90
        facing = (facing - turns) % 4
        for turns in range(int(amount / 90)):
            tempnorth = waypointeast
            waypointeast = -waypointnorth
            waypointnorth = tempnorth
    elif  type == 'F':
        if facing == 0:
            distanceeast += amount
        elif facing == 1:
            distancenorth -= amount
        elif facing == 2:
            distanceeast -= amount
        elif facing == 3:
            distancenorth += amount
        positioneast += amount * waypointeast
        positionnorth += amount * waypointnorth

print(abs(distanceeast) + abs(distancenorth))
print(abs(positionnorth) + abs(positioneast))
