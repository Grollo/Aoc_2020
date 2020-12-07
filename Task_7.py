input = open('input', 'r').readlines()
input = [n.strip() for n in input]

containers = []
contents = []
numbers = []

for line in input:
    lineparts = line.split(' bags contain ')
    container = lineparts[0]
    if lineparts[1] != 'no other bags.':
        content = lineparts[1][:-1]
        for subcontent in content.split(', '):
            colour = subcontent
            if colour.endswith('s'):
                colour = colour[:-1]
            colour = colour[2:-4]
            containers.append(container)
            contents.append(colour)
            numbers.append(int(subcontent[:1]))

baglist = ['shiny gold']
previousbaglistsize = 0
while previousbaglistsize != len(baglist):
    previousbaglistsize = len(baglist)
    for i in range(len(containers)):
        if contents[i] in baglist and not containers[i] in baglist:
            baglist.append(containers[i])

print(len(baglist)-1)

def mustcontain(bag):
    total = 1
    for i in range(len(containers)):
        if containers[i] == bag:
            total += numbers[i] * mustcontain(contents[i])
    return total

print(mustcontain('shiny gold')-1)
