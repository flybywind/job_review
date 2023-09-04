# https://leetcode.cn/problems/graph-valid-tree/solutions/2365993/chao-hao-li-jie-de-bing-cha-ji-tao-lu-by-oa0r/
from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 忽视了一个很重要的条件，即对于树来说，节点数总是等于边数+1，这是一个必要条件。
        # 当然，反之，边数和节点数相等的情况，不一定是合理的树。
        if len(edges) == 0:
            return n == 1
        
        parent = [-1]*n
        adjDict = {i: [] for i in range(n)}
        adjCnt = {i: 0 for i in range(n)}
        root = edges[0][0]
        noneEmpty = 0
        
        def couterDegree(u):
            nonlocal adjCnt, noneEmpty
            adjCnt[u] += 1
            if adjCnt[u] == 1:
                noneEmpty += 1
        
        for u, v in edges:
            couterDegree(u)
            couterDegree(v)
        if noneEmpty != n:
            return False 
        
        for u, v in edges:
            adjDict[u].append(v)
            adjDict[v].append(u)

        def dfs_find_compact(child) -> int:
            if parent[child] == -1:
                return child
            r = dfs_find_compact(parent[child])
            parent[child] = r 
            return r
        
        nextnodes = [root]

        visited = set()
        while len(nextnodes) > 0:
            pre = nextnodes[0]
            visited.add(pre)
            nextnodes = nextnodes[1:]
            r0 = dfs_find_compact(pre)
            for c in adjDict[pre]:
                if c in visited:
                    continue

                r = dfs_find_compact(c)
                if r0 == r:
                    return False
                parent[c] = pre
                
                nextnodes.append(c)

        return len(visited) == n
    
sol = Solution()

n = 4
edges = [[2,3],[1,0]]
print(f"n = {n}, edges = {edges}, is tree: {sol.validTree(n, edges)}")

n = 4
edges = [[2,3],[1,2], [1, 3]]
print(f"n = {n}, edges = {edges}, is tree: {sol.validTree(n, edges)}")

n = 5
edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
print(f"n = {n}, edges = {edges}, is tree: {sol.validTree(n, edges)}")

n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]
print(f"n = {n}, edges = {edges}, is tree: {sol.validTree(n, edges)}")