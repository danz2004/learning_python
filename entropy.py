#!/usr/bin/env python3
import math
import sys
size = 4
values = [0] * size
entropy = 0
for i in range(1, size + 1):
	values[i - 1] = float(sys.argv[i])
for i in range(size):
	entropy += -(math.log2(values[i]) * values[i])
print(f'{entropy : .3f}')
