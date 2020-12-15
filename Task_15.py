input = [18,11,9,0,5,1]
lastnumber = input[-1]
input = input[:-1]
n = 30000000

lastoccurence = dict()
for i in range(len(input)):
    lastoccurence[input[i]] = i

for i in range(len(input), n-1):
    if not lastnumber in lastoccurence:
        newnumber = 0
    else:
        newnumber = i - lastoccurence[lastnumber]
    
    lastoccurence[lastnumber] = i
    lastnumber = newnumber

print(newnumber)
