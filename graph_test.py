# -*- encoding: utf8 -*-
from graph import *

def test_search_depth():
	G = Graph()
	with open("city_paires.txt") as fid:
		for line in fid:
			from_city, to_city = line.strip().split(",")
			G.insert(Node(from_city), Node(to_city))
			G.insert(Node(to_city), Node(from_city))

	beijing = Node("北京")
	xian = Node("西安")
	G.search_depth(beijing, xian)


if __name__ == "__main__":
	test_search_depth()