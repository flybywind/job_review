
class Solution:
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        dir = set()
        for u, vv in enumerate(adj):
            for v in vv:
                dir.add((u, v))
        def topCmp(i, j) -> int:
            if (i, j) in dir:
                return 1
            elif (j, i) in dir:
                return -1
            
        vetex = sorted(range(V), key=lambda x, y: )