#!/usr/bin/env python3
import sys
import random
seq = sys.argv[1]
j = 0
for x in seq:
    j += 1
w = list(seq)
posA = random.randrange(0, j)
posB = random.randrange(0, j)

