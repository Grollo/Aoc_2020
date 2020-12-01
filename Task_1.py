input = open("input", "r").readlines()
input = [int(n.strip()) for n in input]

for i in range(len(input)):
    for j in range(i, len(input)):
        if input[i] + input[j] == 2020:
            print(input[i] * input[j])
            
        for k in range(j, len(input)):
            if input[i] + input[j] + input[k] == 2020:
                print(input[i] * input[j] * input[k])
