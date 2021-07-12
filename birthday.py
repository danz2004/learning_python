#!/usr/bin/env python3
import random
shared = 0
trial_number = 10000
for i in range(trial_number):
	birthdays = [0] * 365
	for j in range(25):
		date = random.randint(0, 364)
		birthdays[date] += 1
		if birthdays[date] == 2:
			shared += 1
			break
print(f'{shared / trial_number : .3f}')
