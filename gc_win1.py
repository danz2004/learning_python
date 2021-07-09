#!/usr/bin/env python3
seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11
for i in range(len(seq) - w + 1):
	count = 0
	for j in range(i, i + w):
		if seq[j] == 'G' or seq[j] == 'C':
			count += 1
	print(f'{i} {seq[i:i+w]} {(count / w) : .4f}')
