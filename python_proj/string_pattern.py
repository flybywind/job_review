#!/bin/env python
# -*- encoding: utf8 -*-
from numpy.random import randint
# O(n^2)
def longest_type3_force(s):
	n = len(s)
	longest = 0
	longest_start = 0
	for i, c in enumerate(s):
		type_set = set()
		type_set.add(c)
		# 忘记了边界检查，当j == n退出时：
		for j in range(i+1, n):
			type_set.add(s[j])
			type_num = len(type_set)
			if type_num > 3:
				l = j - i
				if l > longest:
					longest_start = i
					longest = l
				break
		# enumeration退出的时候，j == n - 1 !
		if j == n - 1 and type_num <= 3:
			l = n - i
			if l > longest:
				longest_start = i
				longest = l

	return longest_start, longest
# O(3n)
def longest_type3(s):
	last_loc = {}
	longest = 0
	n = len(s)
	longest_start = 0
	start = 0
	for i, c in enumerate(s):
		last_loc[c] = i
		if len(last_loc.keys()) > 3:
			restart = i
			del_k = None
			for k, p in last_loc.items():
				if p < restart:
					restart = p + 1
					del_k = k
			l = i - start
			# 忘记删除！
			del last_loc[del_k]
			if longest < l:
				longest = l
				longest_start = start
			start = restart

	if i == n - 1 and len(last_loc.keys()) <= 3:
		l = n - start
		if longest < l:
			longest = l
			longest_start = start
	return longest_start, longest


test_array = randint(1, 5, 15)
print "test_array: ", ",".join([str(p) for p in test_array])

ls, ll = longest_type3_force(test_array)
print "longest substr[%d,%d]: %s" % (ls, ll+ls-1, test_array[ls:ls+ll])

ls, ll = longest_type3(test_array)
print "longest substr[%d,%d]: %s" % (ls, ll+ls-1, test_array[ls:ls+ll])