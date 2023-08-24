#!/usr/bin/env python3
dna = input("Digite a sua sequência de DNA: ")
seqDNA = dna.upper()
seqLEN = len(seqDNA)
ecori = input("Digite a sequência da sua enzima de restrição EcoRI: ")
ecoRIsite = ecori.upper()
startPos = seqDNA.find(ecoRIsite)
fimstartPos = startPos + len(ecoRIsite)
print("A clivagem inicial se dá em: ", startPos, fimstartPos)
seqDNAinvert = seqDNA[::-1]
ecoRIsiteInvert = ecoRIsite[::-1]
endPos0 = seqDNAinvert.find(ecoRIsiteInvert)
endPos = int(seqLEN) - int(endPos0)
inicioendPos = endPos - len(ecoRIsite)
print("A clivagem final se dá em: ", inicioendPos, endPos)
