# https://leetcode.cn/problems/longest-consecutive-sequence/solutions/276931/zui-chang-lian-xu-xu-lie-by-leetcode-solution/
from typing import List

class Solution:    
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = dict()
        for n in nums:
            counter[n] = 0
        def count_recursive(n):
            if counter[n] == 0:
                if n+1 in counter:
                    counter[n] =  count_recursive(n+1)+1
                else:
                    counter[n] = 1
            return counter[n]
            
        maxv = 0
        for n in counter:
           maxv = max(maxv, count_recursive(n))
        return maxv  

sol = Solution()
nums = []
print(f"solution for {nums} = {sol.longestConsecutive(nums)}")

nums = [100,4,200,1,3,2]
print(f"solution for {nums} = {sol.longestConsecutive(nums)}")

nums = [0,3,7,2,5,8,4,6,0,1]
print(f"solution for {nums} = {sol.longestConsecutive(nums)}")