from typing import List 
from bisect import bisect_left

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        i = 0
        N = len(nums)
        while i < N and nums[i] <= 0:
            v = nums[i]
            j = N-1
            while i <= j-2 and nums[j] >= 0:
                v2 = nums[j]
                v3 = -v-v2 
                p = bisect_left(nums, v3)
                if p == i:
                    if p+1 < N and nums[p+1] == v3:
                        res.append([v, v3, v2])
                elif p > i:
                    if p < j:
                        if nums[p] == v3:
                            res.append([v, v3, v2])
                    else:
                        break
                
                # move j forward
                while j >= 0 and nums[j] == v2:
                    j -= 1
            # move forward until found a new value 
            while i < N and nums[i] == v:
                i+=1
        
        return res
     
sol = Solution()
a = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
print(f"triple Zeros of {a} = {sol.threeSum(a)}")

a = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
print(f"triple Zeros of {a} = {sol.threeSum(a)}")

a = [1,2,-2,-1]
print(f"triple Zeros of {a} = {sol.threeSum(a)}")
a = [-1,1,2,-1,-4]
print(f"triple Zeros of {a} = {sol.threeSum(a)}")

a = [-1,0,1,2,-1,-4]
print(f"triple Zeros of {a} = {sol.threeSum(a)}")

a = [-1,-2, -3, 0, 1,2,4]
print(f"triple Zeros of {a} = {sol.threeSum(a)}")

a = [-1, -1,-2, -3, 0, 1,2,4]
print(f"triple Zeros of {a} = {sol.threeSum(a)}")

a = [-1, -1,-2, -3, 1, 0, 1,2,4]
print(f"triple Zeros of {a} = {sol.threeSum(a)}")

a = [-1, -1, -2, -3, 0, 0, 0, 1,2,4]
print(f"triple Zeros of {a} = {sol.threeSum(a)}")

a = [-1, -1, -2, -2, -3, 0, 0, 0, 1,2,4]
print(f"triple Zeros of {a} = {sol.threeSum(a)}")
         

a = [-1, -1, -2, -2, -3, 0, 0, 0, 1,2,2,4]
print(f"triple Zeros of {a} = {sol.threeSum(a)}")

a = [-1, -1, -2, -2, -4, -3, 0, 0, 0, 1,1, 1,2,2,4]
print(f"triple Zeros of {a} = {sol.threeSum(a)}")