"""
峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。

你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
"""


def findPeakIndex(nums):
    def __recur__(left, right):
        if right - left < 3:
            return right-1
        mid = (left + right) // 2
        # print("recur at", left, right, "mid =", mid)
        if nums[left] < nums[mid] and nums[right-1] < nums[mid]:
            # print("find it", mid)
            return mid

        if nums[left] < nums[mid] and nums[mid] < nums[right-1]:  # in ascend side
            return __recur__(mid, right)
        else:
            return __recur__(left, mid)

    return __recur__(0, len(nums))


nums = [1, 1, 2, 3, 5, 4, 3, 2]
print(f"peak index at {findPeakIndex(nums)} for {nums}")


nums = [1, 1, 2, 3, 1, 5, 4, 3, 2]
print(f"peak index at {findPeakIndex(nums)} for {nums}")

nums = [1, 1, 2, 3, 4, 1, 5, 4, 3, 2]
print(f"peak index at {findPeakIndex(nums)} for {nums}")
