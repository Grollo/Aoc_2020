startingseats = open('input', 'r').readlines()
startingseats = [n.strip() for n in startingseats]

columnlength = len(startingseats[0])
rowlength = len(startingseats)

def inbounds(row, column):
    return row >= 0 and column >= 0 and row < rowlength and column < columnlength

def adjescentseatsoccupied(seats, row, column):
    total = 0
    for r in range(row-1,row+2):
        for c in range(column-1,column+2):
            if inbounds(r, c):
                if  not (r == row and c == column) and seats[r][c] == '#':
                    total += 1
    return total

def firstseatshuffle(seats):
    newseats = []
    for row in range(0, rowlength):
        newrow = ''
        for column in range(0, columnlength):
            if seats[row][column] == '.':
                newrow += ('.')
            elif seats[row][column] == 'L':
                if adjescentseatsoccupied(seats, row, column) == 0:
                    newrow += ('#')
                else:
                    newrow += ('L')
            elif seats[row][column] == '#':
                if adjescentseatsoccupied(seats, row, column) > 3:
                    newrow += ('L')
                else:
                    newrow += ('#')
        newseats.append(newrow)
    return newseats

def visibleseatsoccupied(seats, row, column):
    total = 0
    for rdir in range(-1,2):
        for cdir in range(-1,2):
            if rdir == 0 and cdir == 0:
                continue
            r = row + rdir
            c = column + cdir
            while inbounds(r, c) and seats[r][c] == '.':
                r = r + rdir
                c = c + cdir
            if  inbounds(r, c) and seats[r][c] == '#':
                total += 1
    return total

def secondseatshuffle(seats):
    newseats = []
    for row in range(0, rowlength):
        newrow = ''
        for column in range(0, columnlength):
            if seats[row][column] == '.':
                newrow += ('.')
            elif seats[row][column] == 'L':
                if visibleseatsoccupied(seats, row, column) == 0:
                    newrow += ('#')
                else:
                    newrow += ('L')
            elif seats[row][column] == '#':
                if visibleseatsoccupied(seats, row, column) > 4:
                    newrow += ('L')
                else:
                    newrow += ('#')
        newseats.append(newrow)
    return newseats

def occupied(seats):
    total = 0
    for row in seats:
        total += row.count('#')
    return total

previousseats = startingseats
newseats = firstseatshuffle(startingseats)
while previousseats != newseats:
    previousseats = newseats
    newseats = firstseatshuffle(newseats)

print(occupied(newseats))
    
previousseats = startingseats
newseats = secondseatshuffle(startingseats)
while previousseats != newseats:
    previousseats = newseats
    newseats = secondseatshuffle(newseats)

print(occupied(newseats))
