#!/usr/bin/env python3
seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11
window = ""
count = 0;
for i in range(11):
	window += seq[i]
	if seq[i] == 'G' or seq[i] == 'C':
		count += 1
print(f'{0} {window} {count / 11 : .4f}')
for i in range(1, len(seq) - 10):
	if window[0] == 'G' or window[0] == 'C':
		count -= 1
	if seq[i + 10] == 'G' or seq[i + 10] == 'C':
		count += 1
	window = window[1:] + seq[i + 10]
	print(f'{i} {window} {count / 11 : .4f}')
	
