# https://practice.geeksforgeeks.org/problems/optimal-array--170647/1?page=1&difficulty[]=1&category[]=Arrays&category[]=Strings&sortBy=accuracy
from typing import List
from collections import namedtuple

opInfo = namedtuple('opInfo', ['opNum', 'opPos', 'opNeg', 'target'])

# mathmatical proof: https://math.stackexchange.com/questions/113270/the-median-minimizes-the-sum-of-absolute-deviations-the-ell-1-norm
# 如果知道是median，那其实就很简单了。以后还是不要在这种数学问题上浪费时间了。


class Solution:
    def optimalArray(self, n: int, a: List[int]) -> List[int]:
        # code here
        ans = [0]
        sum1 = 0
        sum2 = 0
        for i in range(1, n):
            if ((i+1) % 2 == 0):
                sum1 += a[i//2]
                sum2 += a[i]
            else:
                sum2 += (a[i]-a[i//2])
            ans.append(sum2-sum1)
        return ans


sol = Solution()
arr = [1, 6, 9, 12]
n = len(arr)
print(f"optimal operation num for array {arr} is {sol.optimalArray(n, arr)}")

arr = [1, 1, 1, 7, 7, 10, 19]
n = len(arr)
print(f"optimal operation num for array {arr} is {sol.optimalArray(n, arr)}")

arr = [-23, 32, 39, 39, 44, 46, 48, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49]
n = len(arr)
print(f"optimal operation num for array {arr} is {sol.optimalArray(n, arr)}")
