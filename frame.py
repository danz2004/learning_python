#!/usr/bin/env python3
dna = 'ATGGCCTTT'
#one skipping by 3 one not
for i in range(len(dna)):
	print(i, i % 3, dna[i])

for i in range(0, len(dna) - 2, 3):
	for j in range(3):
		print(i + j, j, dna[i + j])
