input = open("input", "r").readlines()
validpasswords1 = 0
validpasswords2 = 0

for line in input:
    index1 = line.index("-")
    index2 = line.index(":")
    min = int(line[:index1])
    max = int(line[index1+1:index2-2])
    letter = line[index2-1]
    password = line[index2+2:]
    count = password.count(letter)
    if count <= max and count >= min:
        validpasswords1 = validpasswords1 + 1
    if (password[min-1:min] == letter) != (password[max-1:max] == letter):
        validpasswords2 = validpasswords2 + 1

print(validpasswords1)
print(validpasswords2)
