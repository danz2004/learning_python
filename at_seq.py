#!/usr/bin/env python3
import random
#random.seed(1)
DNA = ""
AT_amount = 0
for i in range(30):
	base = random.randint(1, 10)
	if base == 1 or base == 2 or base == 3:
		DNA += 'A'
		AT_amount += 1
	elif base == 4 or base == 5 or base == 6:
		DNA += 'T'
		AT_amount += 1
	elif base == 7 or base == 8:
		DNA += 'G'
	else:
		DNA += 'C'
print(len(DNA), (AT_amount / len(DNA)), DNA)
