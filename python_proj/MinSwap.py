class Solution:

    # Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, nums):
        # Code here
        n = len(nums)
        numwIdx = sorted([i for i in range(n)], key=lambda x: nums[x])
        swapNum = 0
        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue
            # j: old idx
            # i: new idx
            # 1, 3, 2, 4 (0, 1, 2, 3)
            # 1, 2, 3, 4 (0, 2, 1, 3)
            # 4, 3, 5, 2, 1 (0, 1, 2, 3, 4) ==> (0<->4) 1, 3, 5, 2, 4 ==> (4<->2) 1, 3, 4, 2, 5 ==> (2<->1) 1, 4, 3, 2, 5 ==> 1, 2, 3, 4, 5
            # 1, 2, 3, 4, 5 (4, 3, 1, 0, 2)
            j = numwIdx[i]
            visited[i] = True
            visited[j] = True
            if i == j:
                continue

            startIndx = i
            while True:
                swapNum += 1
                j = numwIdx[j]
                visited[j] = True
                if j == startIndx:
                    break

        return swapNum


sol = Solution()
nums = [1, 2, 3, 5]
print(f"minSwap to sort array {nums} = {sol.minSwaps(nums)}")

nums = [2, 8, 5, 4]
print(f"minSwap to sort array {nums} = {sol.minSwaps(nums)}")

nums = [10, 19, 6, 3, 5]
print(f"minSwap to sort array {nums} = {sol.minSwaps(nums)}")

nums = [13, 1, 5, 3, 6, 11, 10]
print(f"minSwap to sort array {nums} = {sol.minSwaps(nums)}")
