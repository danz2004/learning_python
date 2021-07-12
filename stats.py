#!/usr/bin/env python3
import sys
import math
data = [3, 1, 4, 1, 5]
data.sort()
mean = 0
sd = 0
med = 0;
for i in range(len(data)):
	mean += data[i]
mean /= len(data)
for i in range(len(data)):
	sd += ((mean - data[i]) ** 2)
if(len(data) % 2 == 0):
	med = (data[len(data) // 2] + data[len(data) // 2 + 1]) / 2
else:
	med = data[len(data) // 2]
print(f'Count: {len(data)} \nMinimum: {data[0]} \nMaximum: {data[len(data) - 1]} \nMean: {mean : .2f} \nStd. dev: {math.sqrt(sd / len(data)) : .2f} \nMedian: {med : .2f}')
