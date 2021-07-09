#!/usr/bin/env python3
# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Output with 4 significant figures using whichever method you prefer
# Use no nested loops. Instead, count only the first window
# Then 'move' the window by adding 1 letter on one side
# And subtracting 1 letter from the other side
# Describe the pros/cons of this algorith vs. nested loops
seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11
window = ""
count = 0
for i in range(w):
	window += seq[i]
	if seq[i] == 'G' or seq[i] == 'C':
		count += 1
print(f'{0} {window} {count / w : .4f}')
for i in range(1, len(seq) - w + 1):
	if window[0] == 'G' or window[0] == 'C':
		count -= 1
	if seq[i + w - 1] == 'G' or seq[i + w - 1] == 'C':
		count += 1
	window = window[1:] + seq[i + w - 1]
	print(f'{i} {window} {count / w : .4f}')
	
