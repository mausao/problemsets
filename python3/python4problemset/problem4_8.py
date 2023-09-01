#!/usr/bin/env python3
j = 0
k = 0
sequences = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
sequence1 = []
for x in sequences:
    for y in x:
        j += 1
    k += 1
    print(k, "\t", j, "\t", x)
    w = (j, x)
    sequence1.append(w)
    j = 0
print(sequence1)

