#!/usr/bin/env python3
import sys
import random
genome_size = int(sys.argv[1])
read_number = int(sys.argv[2])
read_length = int(sys.argv[3])
genome = [0] * genome_size
for i in range(read_number):
	start = random.randint(0, genome_size - read_length)
	for start in range(start, start + read_length):
		genome[start] += 1
print(genome)
min = genome[read_length]
max = genome[read_length]
sum = 0
for i in range(read_length, genome_size - 2 * read_length):
	if min > genome[i]:
		min = genome[i]
	if max < genome[i]:
		max = genome[i]
	sum += genome[i]
print(f'{min} {max} {sum / (genome_size - 2 * read_length) : .4f}')
