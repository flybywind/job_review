import heapq


class Solution:
    # Function to return the sorted array.
    # https://www.geeksforgeeks.org/nearly-sorted-algorithm/
    def nearlySorted(self, a, n, k):
        i = 0
        s = a[:k+1]
        end = k+1
        heapq.heapify(s)
        while end < n:
            e = heapq.heappop(s)
            heapq.heappush(s, a[end])
            a[i] = e
            i += 1
            end += 1

        while i < n:
            e = heapq.heappop(s)
            a[i] = e
            i += 1
        return a

    def smallestSumSubarray(self, A, N):
        i = 0
        sum = A[i]
        minms = min(A)
        while True:
            if sum < minms:
                minms = sum
            i += 1
            if i < N:
                sum = A[i] if sum > 0 else A[i] + sum
            else:
                break
        return minms

    def subarrayRanges(self, N, arr):
        arr2 = sorted(arr)
        return sum(v*i - v*(N-i-1) for (i, v) in enumerate(arr2))


sol = Solution()
k = 3
arr = [6, 5, 3, 2, 8, 10, 9]
print(f"arr = {arr}, sorted = {sol.nearlySorted(arr, len(arr), k)}")

k = 2
arr = [3, 1, 4, 2, 5]
print(f"arr = {arr}, sorted = {sol.nearlySorted(arr, len(arr), k)}")

k = 1
arr = [5]
print(f"arr = {arr}, sorted = {sol.nearlySorted(arr, len(arr), k)}")

# arr = [3, -4, 2, -3, -1, 7, -5]
# print(
#     f"min-sum of consecutive sub array of {arr} is {sol.smallestSumSubarray(arr, len(arr))}")

# arr = [2, 6, 8, 1, 4]
# print(
#     f"min-sum of consecutive sub array of {arr} is {sol.smallestSumSubarray(arr, len(arr))}")

# arr = [443, -807, -533, 544, 271, -81, -200, -502, 71, 622, -496, 109, -862, 306, -705, 724, -672, 920, 864, -150, -629, -22, 976, 237, -219, 740, 705, 570, 257, -369, -932, 663, 36, -750, -792, 445, -101, 128, -48, 38, -513, 426, 850, -973, -745,
#        593, -73, 993, -48, 535, 732, 485, 631, -353, 277, -227, 60, 840, -667, -860, -86, -540, 161, -298, 939, 892, 741, 999, -722, -167, 170, -723, -754, -895, -70, -305, 225, -752, -404, -66, -733, -726, 282, -705, -831, 420, 868, -45, -747, -181, 304, -515]
# print(
#     f"min-sum of consecutive sub array of {arr} is {sol.smallestSumSubarray(arr, len(arr))}")

# arr = [1, 2, 3]
# print(f"sum of range of array {arr} = {sol.subarrayRanges(len(arr), arr)}")

# arr = [-32, 0, -2, 72]
# print(f"sum of range of array {arr} = {sol.subarrayRanges(len(arr), arr)}")
