input = open('input', 'r').readlines()
input = [n.strip().replace(' ', '') for n in input]

def findmatching(expression, left):
    nestedvalue = 1
    for char in range(left+1, len(expression)):
        if expression[char] == '(':
            nestedvalue += 1
        elif expression[char] == ')':
            nestedvalue -= 1
            if nestedvalue == 0:
                return char

def evaluate(expression):
    char = 0
    while char < len(expression):
        if expression[char] == '(':
            matchingrightparen = findmatching(expression, char)
            equivalent = evaluate(expression[char+1:matchingrightparen])
            expression = expression[:char] + str(equivalent) + expression[matchingrightparen+1:]
        char += 1

    char = 0
    while expression[char] != '+' and expression[char] != '*':
        char += 1
    total = int(expression[:char])
    while char < len(expression):
        nextchar = char+2
        while nextchar < len(expression) and expression[nextchar] != '+' and expression[nextchar] != '*':
            nextchar += 1

        if expression[char] == '+':
            total += int(expression[char+1:nextchar])
        else:
            total *= int(expression[char+1:nextchar])

        char = nextchar

    return total

def evaluate2(expression):
    char = 0
    while char < len(expression):
        if expression[char] == '(':
            matchingrightparen = findmatching(expression, char)
            equivalent = evaluate2(expression[char+1:matchingrightparen])
            expression = expression[:char] + str(equivalent) + expression[matchingrightparen+1:]
        char += 1

    mults = expression.split('*')
    product = 1
    for mult in mults:
        additions = mult.split('+')
        partialsum = 0
        for number in additions:
            partialsum += int(number)
        product *= partialsum
    return product

sum = 0
for line in input:
    sum += evaluate(line)
print(sum)

sum = 0
for line in input:
    sum += evaluate2(line)
print(sum)
