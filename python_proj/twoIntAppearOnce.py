from typing import List
from functools import reduce
# https://leetcode.cn/problems/single-number-iii/submissions/456863698/
# 异或运算和与负运算的典型案例
# a ^ b ^ b = a
# a & -a 等于a中，保留最低位的1时，表示的数字，比如x = 12 = 0b1100, 那么a & -a = 4
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # select one pivot, left element < pivot, right >= pivot
        # if |left| and |right| are both even, then xor all elements of left and right side
        # if XOR(left) == 0, then find in right; or find in left
        # if only one side is odd, then only find in the odd side
        def _find_recur(nums: List[int], left: int, right: int) -> List[int]:
            if right - left == 1:
                return [nums[left]]
            if right - left == 2:
                if nums[left] != nums[right-1]:
                    return nums[left:right]
                else:
                    return []
            
            pivot = nums[(left+right)//2]
            if nums[left] > nums[right-1]: # ensure nums[left] <= nums[right-1]
                nums[left], nums[right-1] = nums[right-1], nums[left]
            if pivot <= nums[left]: # ensure pivot bigger than left, so the left size should not be zero. or we may fall into endless loop
                pivot = nums[right-1]

            i, j = left, right-1
            while i < j: # o(n)
                while i < j and nums[i] < pivot:
                    i+=1
                while j > i and nums[j] >= pivot:
                    j-=1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    break
            size0 = i - left 
            size1 = right - i

            if size0%2 == 0 and size1%2 == 0:
                xor0 = reduce(lambda x, y: x^y, nums[left:i])
                xor1 = reduce(lambda x, y: x^y, nums[i:right])
                if xor0 != 0:
                    return _find_recur(nums, left, i)
                elif xor1 != 0:
                    return _find_recur(nums, i, right)
                else:
                    return []
            else:
                ret = []
                if size0%2 == 1:
                    ret += _find_recur(nums, left, i)
                if size1%2 == 1:
                    ret += _find_recur(nums, i, right)
                return ret
        
        return _find_recur(nums, 0, len(nums))
    

sol = Solution()
nums = [43772400,1674008457,1779561093,744132272,1674008457,448610617,1779561093,124075538,-1034600064,49040018,612881857,390719949,-359290212,-812493625,124732,-1361696369,49040018,-145417756,-812493625,2078552599,1568689850,865876872,865876872,-1471385435,1816352571,1793963758,2078552599,-1034600064,1475115274,-119634980,124732,661111294,-1813882010,1568689850,448610617,1347212898,-1293494866,612881857,661111294,-1361696369,1816352571,-1813882010,-359290212,1475115274,1793963758,1347212898,43772400,-1471385435,124075538,-1293494866,-119634980,390719949]
print(f"find num only appear once from {nums}: {sol.singleNumber(nums)}")

# nums = [1,2,1,3,2,5]
# print(f"find num only appear once from {nums}: {sol.singleNumber(nums)}")

# nums = [1,2,3,1,2,5]
# print(f"find num only appear once from {nums}: {sol.singleNumber(nums)}")

# nums = [1,0, 2, 0, 3,1,4,4,2,5]
# print(f"find num only appear once from {nums}: {sol.singleNumber(nums)}")

# nums = [1,0, 2, 0, 3,1,4,7,4,2,5, 7]
# print(f"find num only appear once from {nums}: {sol.singleNumber(nums)}")