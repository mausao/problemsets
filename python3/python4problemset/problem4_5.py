#!/usr/bin/env python3
list = [101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]
sumPar = 0
sumImpar = 0
for x in list:
    print("O número testado é ", x)
    if x % 2 == 0:
        print("O número é par")
        sumPar += x
    else:
        print("O número é ímpar")
        sumImpar += x
print("Sum of even number: ", sumPar)
print("Sum of odds: ", sumImpar)

