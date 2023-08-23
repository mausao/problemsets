#!/usr/bin/env python3
seqDNA = input("Digite a sua sequência de DNA: ")
default = seqDNA.upper()
complement = ""
print("Original sequence:\t5'\t", default,"\t3'")
for x in default:
    if x =="A":
        complement += "T"
    elif x =="T":
        complement += "A"
    elif x == "C":
        complement += "G"
    else:
        complement += "C"
print("Complement:\t\t3'\t", complement,"\t5'")
reverse_complement = complement[::-1]
print("Reverse complement:\t5'\t", reverse_complement,"\t3'")

