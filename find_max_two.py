#!/bin/env python
# -*- encoding: utf8 -*-
# 给定一个数组，寻找里面和最大的2个数
from numpy.random import randint
# 暴力方法寻找
def find_max_two_force(vec):
	N = len(vec)
	Max = 0
	i1, i2 = (0, 0)
	for i, v in enumerate(vec):
		for j in range(i + 1, N):
			max_cur = v + vec[j]
			if max_cur > Max:
				i2 = j
				i1 = i
				Max = max_cur
	return Max, i1, i2


def find_max_two(vec, i1, i2):
	N = i2 - i1
	if N > 2:
		mid = int((i1 + i2) / 2)
		m1 = find_max_two(vec, i1, mid)
		m2 = find_max_two(vec, mid, i2)
		m3 = max(vec[:mid]) + max(vec[mid:])
		if m1 is None:
			return max(m2, m3)
		elif m2 is None:
			return max(m1, m3)
		else:
			return max([m1, m2, m3])
	elif N == 1:
		return None
	else:
		return sum(vec[i1:i2])

if __name__ == "__main__":
	sample = randint(-100, 100, 10)
	print "sample is ", sample
	print "max two result:", find_max_two_force(sample)
	print "max two: ", find_max_two(sample, 0, len(sample))