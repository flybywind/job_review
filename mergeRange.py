# https://leetcode.cn/problems/merge-intervals/
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        ret = [intervals[0]]
        
        def isOverlap(t1, t2) -> bool:
            return t2[0] <= t1[1]
        
        for intv in intervals[1:]:
            if isOverlap(ret[-1], intv):
                ret[-1][1] = max(ret[-1][1], intv[1])
            else:
                ret.append(intv)
        return ret
    
sol = Solution()
intervals = [[1,2]]
print(f"solution of {intervals} is {sol.merge(intervals)}")

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(f"solution of {intervals} is {sol.merge(intervals)}")

intervals = [[1,4],[4,5]]
print(f"solution of {intervals} is {sol.merge(intervals)}")