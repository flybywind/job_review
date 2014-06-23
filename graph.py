# -*- encoding: utf8 -*-
class Node:
	def __init__(self, name):
		self.name = name
		self.visited = False
	def __str__(self):
		return str(self.name)
	def __eq__(self, other):
		return str(self) == str(other)
	def __hash__(self):
		return hash(str(self))

class Graph:
	def __init__(self):
		self._edges_ = {}
		self._search_stack_ = list()

	def insert(self, from_v, to_v):
		if from_v in self._edges_:
			self._edges_[from_v].add(to_v)
		else:
			self._edges_[from_v] = set([to_v,])

	def search_depth(self, src, dest):
		self._search_stack_.append(src)
		# 因为是双向边，这个标志位防止往回遍历
		src.visited = True
		for n in self._edges_[src]:
			if n == dest:
				print " -- ".join(self._search_stack_) + " -- " + n
			elif not n.visited:
				self.search_depth(n, dest)

		self._search_stack_.pop()

	def __clear_stack__(self):
		del self._search_stack_
		self._search_stack_ = list()