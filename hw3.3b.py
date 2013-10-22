import math, matplotlib.pyplot as plt, random

total = 0.00
alpha = 0.1
z = 64
bits = 10
ibit = 7 -1
num = 0.00
denom = 0.00

for n in range (100000):
    binary = []
    decimal = 0
    power = 0.00
    for i in range (bits):
        rand = 1 if (random.random() > .5) else 0
        binary.append(rand)
    for bit in range (len(binary)):
        decimal += math.pow(2, bit)*binary[bit]

    indicator = binary[ibit]
    power = pow(alpha, math.fabs(z - decimal))
    prob = (float(1-alpha)/float(1+alpha))*power
    print "%i*%e*%e" %(indicator,prob,power)
    num += indicator*prob
    denom += prob
    print "total = %e/%e" %(num,denom)
    print binary
    print "Deci = %d" %(decimal)
    print "prob = %e" %(prob)
    print "powe = %e" %(power)
        
total += float(num)/float(denom) if (denom > 0) else 0
print "total = %f" %(total)
                                   



