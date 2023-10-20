# https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1?page=1&difficulty[]=1&sortBy=submissions
# 5, 8, 1, 10, K = 2
#
#
class Solution:
    def minDiff(self, arr, n, k):
        if n == 1:
            return 0
        arr2 = sorted(arr)
        if arr2[-1] <= k:
            return arr2[-1] - arr2[0]

        # find left start
        j = 1
        minLeft = maxLeft = arr2[0]+k
        while arr2[j] < k:
            maxLeft = arr2[j]+k
            j += 1

        minRight, maxRight = arr2[j]-k, arr2[-1]-k
        minDiff = max(maxLeft, maxRight) - min(minLeft, minRight)
        for i in range(j, n+1):
            maxLeft = arr2[i-1]+k
            if i == n:
                minRight = maxRight = maxLeft
            else:
                minRight = arr2[i]-k
            curDiff = max(maxLeft, maxRight) - min(minLeft, minRight)
            if curDiff < minDiff:
                minDiff = curDiff
        return minDiff


sol = Solution()
arr = [1, 9]
k = 7
n = len(arr)
print(f"min diff after mod {k} of {arr} is {sol.minDiff(arr, n, k)}")  # 6

arr = [1, 9]
k = 4
n = len(arr)
print(f"min diff after mod {k} of {arr} is {sol.minDiff(arr, n, k)}")  # 0

arr = [5, 5, 8, 6, 4, 10, 3, 8, 9, 10]
k = 5
n = len(arr)
print(f"min diff after mod {k} of {arr} is {sol.minDiff(arr, n, k)}")  # 7

arr = [6, 1, 9, 1, 1, 7, 9, 5, 2, 10]
k = 4
n = len(arr)
print(f"min diff after mod {k} of {arr} is {sol.minDiff(arr, n, k)}")  # 5


arr = [5, 8, 1, 10]
k = 2
n = len(arr)
print(f"min diff after mod {k} of {arr} is {sol.minDiff(arr, n, k)}")  # 5

arr = [3, 9, 12, 16, 20]
k = 3
n = len(arr)
print(f"min diff after mod {k} of {arr} is {sol.minDiff(arr, n, k)}")  # 11

arr = [2, 6, 3, 4, 7, 2, 10, 3, 2, 1]
k = 5
n = len(arr)
print(f"min diff after mod {k} of {arr} is {sol.minDiff(arr, n, k)}")  # 7
