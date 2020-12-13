from math import gcd

input = open('input', 'r').readlines()
input = [n.strip() for n in input]

mytime = int(input[0])
buses = input[1].split(',')

busesinservice = []
waittimes = []
offsets = []

for i in range(len(buses)):
    bus = buses[i]
    if bus == 'x':
        continue
    interval = int(bus)
    missedbuses = int(mytime / interval)
    nextbus = (missedbuses + 1) * interval
    waittime = nextbus - mytime
    busesinservice.append(interval)
    waittimes.append(waittime)
    offsets.append(i)

index = waittimes.index(min(waittimes))
print(busesinservice[index] * waittimes[index])

def eulerphi(n):
    coprimes = 0        
    for i in range(1, n+1):
        if gcd(n, i) == 1:
            coprimes += 1
    return coprimes

busproduct = 1
for bus in busesinservice:
    busproduct *= bus
sum = 0
for i in range(len(busesinservice)): # Chinese remainder theorem
    bus = busesinservice[i]
    remainder = (bus - offsets[i]) % bus
    b = int(busproduct / bus) ** (eulerphi(bus) - 1) % bus
    sum += b * remainder * int(busproduct / bus)

print(sum % busproduct)
