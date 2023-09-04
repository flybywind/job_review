from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        red, green = 0, 1
        nodeNum = len(graph)
        nodeColor = [-1]*nodeNum
        cand = [0]

        while len(cand) > 0:
            i = cand[0]
            cand = cand[1:]

            v = graph[i]
            if nodeColor[i] == -1:
                nodeColor[i] = red
                other = green
            else:
                other = (nodeColor[i]+1)%2
            
            for u in v:
                if nodeColor[u] != -1:
                    if nodeColor[u] != other:
                        return False
                else:
                    nodeColor[u] = other
                    cand.append(u)
            if len(cand) == 0:
                for j, c in enumerate(nodeColor):
                    if c == -1:
                        cand.append(j) 
                        break   
        # further validate it
        for i, v in enumerate(graph):
            c = nodeColor[i]
            for u in v:
                if nodeColor[u] == c:
                    return False

        return True
    
if __name__ == "__main__":
    sol = Solution()
    graph = [[],[2],[1],[],[],[7,8],[7,8,9],[5,6],[5,6],[6],[12,13,14],[12],[10,11],[10],[10],[18],[17,18],[16],[15,16],[],[22,23,24],[22,23,24],[20,21],[20,21],[20,21],[27,28,29],[27,28,29],[25,26],[25,26],[25,26],[32,33,34],[33],[30],[30,31],[30],[37,39],[38],[35],[36],[35],[44],[43,44],[],[41],[40,41],[47,48,49],[47,48,49],[45,46],[45,46],[45,46]]
    print(f"try finding bipart from graph: {graph}, {sol.isBipartite(graph)}")
    
    graph = [[4],[],[4],[4],[0,2,3]]
    print(f"try finding bipart from graph: {graph}, {sol.isBipartite(graph)}")
    
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    print(f"try finding bipart from graph: {graph}, {sol.isBipartite(graph)}")

    graph = [[1,3],[0,2],[1,3],[0,2]]
    print(f"try finding bipart from graph: {graph}, {sol.isBipartite(graph)}")

    graph = [[3],[2,4],[1],[0,4],[1,3]]
    print(f"try finding bipart from graph: {graph}, {sol.isBipartite(graph)}")