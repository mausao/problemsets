#!/usr/bin/env python3
seqDNA = input("Digite a sua sequência de DNA: ")
default = seqDNA.upper()
ATcontent = 0
CGcontent = 0
for x in default:
    if (x == "A") or (x == "T"):
        ATcontent += 1
    else:
        CGcontent += 1
print("A quantidade de AT na sequência é:", ATcontent)
print("A quantidade de CG na sequência é:", CGcontent)

