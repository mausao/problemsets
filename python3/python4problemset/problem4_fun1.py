#!/usr/bin/env python3
import sys
import random
seq = sys.argv[1]
j = 0
for x in seq:
    j += 1
w = list(seq)
print(w)
posA = random.randrange(0, j)
posB = random.randrange(0, j)
if posA == posB:
    posA = random.randrange(0, j)
    posB = random.randrange(0, j)
else:
    print(posA, posB)
    letra1 = w[posA]
    letra2 = w[posB]
    print(letra1, letra2)
    w.insert(posA, letra2)
    posA += 1
    w.pop(posA)
    w.insert(posB, letra1)
    posB += 1
    w.pop(posB)
    print(w)
