#!/usr/bin/env python3
try:
    num = int(input("Digite um número: "))
    even = num/2
    if num > 0:
        print("O número digitado é positivo!")
        if num < 50:
            print("O número além de positivo é menor do que 50!")
            if even == int(even):
                print("O numéro além de positivo e menor do que 50 também é par!")
        elif num > 50:
            print("O número é maior do que 50!")
            if num % 3 == 0:
                print("O número além de maior que 50 também é divisível por 3!")
    elif num == 0:
        print("O número digitado é 0! Positivo ou negativo?")
    else: 
        print("O número digitado é negativo!")
except ValueError:
    print("Oops! Digite um número válido!")
