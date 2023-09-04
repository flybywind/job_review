from typing import List
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Function to return list containing vertices in Topological order.
        in_degree_map = {x:0 for x in range(numCourses)}

        next_courses_map = defaultdict(list)
        for u, v in prerequisites:
            in_degree_map[u] += 1
            next_courses_map[v].append(u)

        queue = []
        # first put the course nodes of zero in-degree
        for n, d in in_degree_map.items():
            if d == 0:
                queue.append(n)

        res = []
        def dfs(n):
            res.append(n)
            for child in next_courses_map[n]:
                in_degree_map[child] -= 1
                if in_degree_map[child] == 0:
                    dfs(child)

        for n in queue:
            dfs(n)

        return res if len(res) == numCourses else []

sol = Solution()    
numCourses = 1
prerequisites = []
print(f"Can finish {numCourses} courses, given dependences {prerequisites}: {sol.findOrder(numCourses, prerequisites)}")

numCourses = 2
prerequisites = [[1,0]]
print(f"Can finish {numCourses} courses, given dependences {prerequisites}: {sol.findOrder(numCourses, prerequisites)}")

numCourses = 2
prerequisites = [[1,0], [0,1]]
print(f"Can finish {numCourses} courses, given dependences {prerequisites}: {sol.findOrder(numCourses, prerequisites)}")

numCourses = 7
prerequisites = [[0, 1], [0,2], [0, 3], [1, 4], [4, 5], [2, 6], [3, 6], [5, 0]]
print(f"Can finish {numCourses} courses, given dependences {prerequisites}: {sol.findOrder(numCourses, prerequisites)}")

numCourses = 7
prerequisites = [[0, 1], [0,2], [0, 3], [1, 4], [3, 6], [2, 6], [4, 5]]
print(f"Can finish {numCourses} courses, given dependences {prerequisites}: {sol.findOrder(numCourses, prerequisites)}")

numCourses = 7
prerequisites = [[0, 1], [0,2], [2, 4], [0, 3], [1, 4], [3, 6], [2, 6], [4, 5]]
print(f"Can finish {numCourses} courses, given dependences {prerequisites}: {sol.findOrder(numCourses, prerequisites)}")

prerequisites = [[0, 1], [0,2], [2, 4], [0, 3], [1, 4], [3, 6], [6, 2], [4, 5]]
print(f"Can finish {numCourses} courses, given dependences {prerequisites}: {sol.findOrder(numCourses, prerequisites)}")

prerequisites = [[0, 1], [0,2], [2, 4], [0, 3], [1, 4], [3, 6], [6, 2], [4, 5], [5, 6]]
print(f"Can finish {numCourses} courses, given dependences {prerequisites}: {sol.findOrder(numCourses, prerequisites)}")

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(f"Can finish {numCourses} courses, given dependences {prerequisites}: {sol.findOrder(numCourses, prerequisites)}")