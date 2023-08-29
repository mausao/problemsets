#!/usr/bin/env python3
##v = 1000
##y = 0
##while v > 1:
##    y += v * (v-1)
##    v -= 1
##print("O fatorial de 1000 é ", y)
##O que está errado?

v = 1000
fat = 1 
while v > 1:
    fat *= v
    v -= 1
print("resposta: ", fat)
