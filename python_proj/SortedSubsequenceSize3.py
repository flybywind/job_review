class Solution:
    def find3number(self, A, n):
        # code here
        if n < 3:
            return []
        # min num in left side of i
        minarr = [0] * n
        # max num in right side of i
        maxarr = [0] * n
        minarr[1] = 0
        maxarr[n-2] = n-1
        for i in range(2, n-1):
            minarr[i] = minarr[i-1] if A[minarr[i-1]] <= A[i-1] else i-1
        for i in range(n-3, 0, -1):
            maxarr[i] = maxarr[i+1] if A[i+1] <= A[maxarr[i+1]] else i+1
        for i in range(1, n-1):
            if A[i] > A[minarr[i]] and A[i] < A[maxarr[i]]:
                return [A[minarr[i]], A[i], A[maxarr[i]]]
        return []


sol = Solution()

arr = [1, 2, 1, 1, 3]
print(f"sort num3 of {arr} is in {sol.find3number(arr, len(arr))}")

arr = [1, 1, 1, 3]
print(f"sort num3 of {arr} is in {sol.find3number(arr, len(arr))}")

arr = [4, 1, 5, 2, 1, 3, 3]
print(f"sort num3 of {arr} is in {sol.find3number(arr, len(arr))}")

arr = [4, 1, 5, 2, 1, 6, 3]
print(f"sort num3 of {arr} is in {sol.find3number(arr, len(arr))}")

arr = [4, 1, 5, 2, 1, 6, 1]
print(f"sort num3 of {arr} is in {sol.find3number(arr, len(arr))}")

arr = [7, 6, 5, 4, 8, 9, 1]
print(f"sort num3 of {arr} is in {sol.find3number(arr, len(arr))}")
