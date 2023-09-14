#!/usr/bin/env python3
ano = input("Digite o ano que deseja saber se é bi: ")
ano = int(ano)
if (((ano % 4 == 0) and (ano % 100 != 0)) or ano % 400 == 0):
    print("O ano é bi!")
else:
    print("O ano não é bi!")
