#!/usr/bin/env python3
amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
for i in range(len(amino_acids) - 1):
	for j in range(i + 1, len(amino_acids)):
		print(amino_acids[i], amino_acids[j])

