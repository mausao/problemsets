#!/usr/bin/env python3
import sys
seqDNA = input("Digite a sua sequência: ")
contemSEQ = input("Qual é o códon que você deseja verificar se está contido na sequência acima? ")
if contemSEQ in seqDNA:
    print("O códon fornecido está presente na sequência")
else:
    print("O códon fornecido não está presente na sequência")
