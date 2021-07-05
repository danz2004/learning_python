#!/usr/bin/env python3
dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
count = 0
for i in range(len(dna)):
	if dna[i] == 'C' or dna[i] == 'G':
		count += 1
print(f'{count / len(dna) : .2f}')
