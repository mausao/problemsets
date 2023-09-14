#!/usr/bin/env python3
seq = input("Digite a sua sequência: ")
resp = {}
for nt in seq:
    if nt in resp:
        resp[nt] += 1
    else:
        resp[nt] = 1
print(resp)
print("O conteúdo GC da sequência é: ", resp['C'] + resp['G'], "ou em %: ", (resp['C'] + resp['G']) / (resp['A'] + resp['T'] + resp['C'] + resp ['T']))
