#!/usr/bin/env python3
import sys
value1 = sys.argv[1]
value2 = sys.argv[2]
print("Os números ímpares contidos no intervalo cedido são\n")
for x in range(int(value1), int(value2)):
    if x % 2 == 1:
        print(x)
