from typing import List 

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        i = 1
        res = sum(nums[:3])
        mingap = abs(target - res)
        while i < len(nums)-1:
            left, right = i-1, i+1
            while left >= 0 and right < len(nums):
                s = nums[i] + nums[left] + nums[right]
                gap = abs(target-s)
                if gap < mingap:
                    mingap = gap
                    res = s
                # move right to increase s
                if target > s:
                    right += 1
                elif target < s:
                    left -= 1 
                else: 
                    return target
            i += 1

        return res

sol = Solution()
nums = [-1,2,1,-4]
target = 1
print(f"three sum closest to {target} in {nums} is {sol.threeSumClosest(nums, target)}")

nums = [0,0,0]
target = 1
print(f"three sum closest to {target} in {nums} is {sol.threeSumClosest(nums, target)}")

nums = [-1, 2, 1, 1, -4]
target = 1
print(f"three sum closest to {target} in {nums} is {sol.threeSumClosest(nums, target)}")

nums = [0,0,0, 1, 2, -1]
target = 1
print(f"three sum closest to {target} in {nums} is {sol.threeSumClosest(nums, target)}")

nums = [-1, 2, 1, 1, -4]
target = 3
print(f"three sum closest to {target} in {nums} is {sol.threeSumClosest(nums, target)}")

nums = [-1, 2, 1, 1, -4]
target = -3
print(f"three sum closest to {target} in {nums} is {sol.threeSumClosest(nums, target)}")