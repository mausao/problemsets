#!/usr/bin/env python3
seqDNA = input("Digite a sua sequência de DNA: ")
default = seqDNA.upper()
substring = default[100:200]
Gcontent = substring.count("G")
print("A sua substring - do nt 100 ao 200 é:", substring, "\nO conteúdo de guanina nessa subsequência é de:", Gcontent)
