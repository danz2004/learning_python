#!/usr/bin/env python3
import random
birthdays = [0] * 365
shared = 0;
is_shared = False
for i in range(10000):
	for j in range(25):
		date = random.randint(0, 364)
		birthdays[date] += 1
		if birthdays[date] == 2 and is_shared == False:
			shared += 1
			is_shared = True
	is_shared = False
	birthdays = [0] * 365
print(f'{shared / 10000 : .3f}')
