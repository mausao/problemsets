#!/usr/bin/env python3
try:
    num = int(input("Digite um número: "))
    if num > 0:
        print("O número digitado é positivo!")
        if num < 50:
            print("O número além de positivo é menor do que 50!")
            if (num/2 == 0) or (num == 2):
                print("O numéro além de positivo e menor do que 50 também é par!")
    elif num == 0:
        print("O número digitado é 0! Positivo ou negativo?")
    else: 
        print("O número digitado é negativo!")
except ValueError:
    print("Oops! Digite um número válido!")
