# -*- encoding: utf8 -*-
from graph import *

def test_search_depth():
	G = Graph()
	node_dict = {}
	with open("city_paires.txt") as fid:
		for line in fid:
			from_city, to_city = line.strip().split(",")
			# 必须保存引用
			if from_city in node_dict:
				from_node = node_dict[from_city]
			else:
				from_node = Node(from_city)
				node_dict[from_city] = from_node
			if to_city in node_dict:
				to_node = node_dict[to_city]
			else:
				to_node = Node(to_city)
				node_dict[to_city] = to_node

			G.insert(from_node, to_node)
			G.insert(to_node, from_node)

	beijing = node_dict["杭州"]
	xian = node_dict["北京"]
	G.search_depth(beijing, xian)


if __name__ == "__main__":
	test_search_depth()
# output:
# 杭州 -- 天津 -- 北京
# 杭州 -- 北京
# 杭州 -- 成都 -- 北京
# 杭州 -- 成都 -- 西安 -- 北京