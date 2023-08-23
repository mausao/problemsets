#!/usr/bin/env python3
import sys
seqDNA = input("Digite a sua sequência de DNA: ")
default = seqDNA.upper()
A = seqDNA.count("A")
T = seqDNA.count("T")
C = seqDNA.count("C")
G = seqDNA.count("G")
print("A quantidade de adenosinas na sua sequência é:", A, "\nA quantidade de timinas na sua sequência é:", T, "\nA quantidade de guaninas na sua sequência é:", G, "\nA quantidade de citosinas na sua sequência é:", C, "\n")
print("A sua sequência de DNA após o processo transcricional (mRNA) é:",default.replace('T','U'))
