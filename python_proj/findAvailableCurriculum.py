# https://leetcode.cn/problems/course-schedule/
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqmap = {a:[] for a in range(numCourses)}
        for a, b in prerequisites:
            prereqmap[a].append(b)

        checkCache = set()
        # DFS
        def checkDep(visited, depsStack) -> bool:
            for next in depsStack:
                if next in visited:
                    return False
                if next in checkCache:
                    continue
                visited.add(next)
                if not checkDep(visited, prereqmap[next]):
                    return False
                checkCache.add(next)
                visited.remove(next)
            return True

        for c, deps in prereqmap.items():
            visited = set([c])
            if c in checkCache:
                continue
            if not checkDep(visited, deps) :
                return False
            checkCache.add(c)
        return True

sol = Solution()    
numCourses = 2
prerequisites = [[1,0]]
print(f"Can finish {numCourses} courses, given dependences {prerequisites}: {sol.canFinish(numCourses, prerequisites)}")

numCourses = 2
prerequisites = [[1,0], [0,1]]
print(f"Can finish {numCourses} courses, given dependences {prerequisites}: {sol.canFinish(numCourses, prerequisites)}")

numCourses = 7
prerequisites = [[0, 1], [0,2], [0, 3], [1, 4], [4, 5], [2, 6], [3, 6], [5, 0]]
print(f"Can finish {numCourses} courses, given dependences {prerequisites}: {sol.canFinish(numCourses, prerequisites)}")

numCourses = 7
prerequisites = [[0, 1], [0,2], [0, 3], [1, 4], [3, 6], [2, 6], [4, 5]]
print(f"Can finish {numCourses} courses, given dependences {prerequisites}: {sol.canFinish(numCourses, prerequisites)}")

numCourses = 7
prerequisites = [[0, 1], [0,2], [2, 4], [0, 3], [1, 4], [3, 6], [2, 6], [4, 5]]
print(f"Can finish {numCourses} courses, given dependences {prerequisites}: {sol.canFinish(numCourses, prerequisites)}")

prerequisites = [[0, 1], [0,2], [2, 4], [0, 3], [1, 4], [3, 6], [6, 2], [4, 5]]
print(f"Can finish {numCourses} courses, given dependences {prerequisites}: {sol.canFinish(numCourses, prerequisites)}")

prerequisites = [[0, 1], [0,2], [2, 4], [0, 3], [1, 4], [3, 6], [6, 2], [4, 5]]
print(f"Can finish {numCourses} courses, given dependences {prerequisites}: {sol.canFinish(numCourses, prerequisites)}")

prerequisites = [[0, 1], [0,2], [2, 4], [0, 3], [1, 4], [3, 6], [6, 2], [4, 5], [5, 6]]
print(f"Can finish {numCourses} courses, given dependences {prerequisites}: {sol.canFinish(numCourses, prerequisites)}")