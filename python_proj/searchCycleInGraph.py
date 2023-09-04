from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        idxMap = {}
        unvisited = set(range(V))
        start = 0
        pos = 0
        idxMap[start] = pos
        while len(idxMap) <= V:
            neig = adj[start]
            next = start
            for u in neig:
                if u not in idxMap:
                    idxMap[u] = pos+1
                    pos += 1
                    next = u
                    break
                if idxMap[u] != pos-1:
                    return True
            if start in unvisited:
                unvisited.remove(start)
            if next==start:
                if len(unvisited) > 0:
                    next = unvisited.pop()
                if next not in idxMap:
                    idxMap[next] = pos+1
                    pos += 1
                else:
                    break

            start = next
        return False

sol = Solution()    
V = 5
adj = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]] 
print(f"{adj} has cycle: {sol.isCycle(V, adj)}")

V = 4
adj = [[], [2], [1, 3], [2]] 
print(f"{adj} has cycle: {sol.isCycle(V, adj)}")

file = ""