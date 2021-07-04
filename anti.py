#!/usr/bin/env python3
dna = 'ACTGAAAAAAAAAAA'
reverse_dna = ''
for i in range(len(dna)):
	if dna[len(dna) - i - 1] == 'A':
		reverse_dna += 'T'
	elif dna[len(dna) - i - 1] == 'T':
		reverse_dna += 'A'
	elif dna[len(dna) - i - 1] == 'G':
		reverse_dna += 'C'
	elif dna[len(dna) - i - 1] == 'C':
		reverse_dna += 'G'
print(reverse_dna)
