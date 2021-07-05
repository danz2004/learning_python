#!/usr/bin/env python3
seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11
window = ""
count = 0
for i in range(len(seq) - 10):
	for j in range(i, i + 11):
		window += seq[j]
		if seq[j] == 'G' or seq[j] == 'C':
			count += 1
	print(f'{i} {window} {(count / 11) : .4f}')
	window = ""
	count = 0;
