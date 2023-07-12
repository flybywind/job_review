package firstmissingpositive

import "math"

// https://leetcode.cn/problems/first-missing-positive/solution/que-shi-de-di-yi-ge-zheng-shu-by-leetcode-solution/
// 关键是要看到问题的本质属性。这样才能设计好一个高效的算法。
// 对于一个长度为 N 的数组，其中没有出现的最小正整数只能在 [1, N+1]中。这是因为如果 [1, N] 都出现了，那么答案是 N+1，否则答案是 [1,N] 中没有出现的最小正整数。
// in-place sort
func firstMissingPositive(nums []int) int {
	if len(nums) == 1 {
		if nums[0] == 1 {
			return 2
		}
		return 1
	}
	var start_p, next_p = 0, 1
	// find the minimum
	minv := math.MaxInt
	for _, v := range nums {
		if v > 0 && v < minv {
			minv = v
		}
	}
	if minv > 1 {
		return 1
	}
	offset := minv
	for start_p < len(nums) {
		for {
			v := nums[start_p]
			if v-offset < 0 || v-offset == start_p || v-offset >= len(nums) {
				// stop iteration
				start_p, next_p = next_p, next_p+1
				break
			}
			if v == nums[v-offset] {
				nums[v-offset] = -1
			}
			nums[start_p], nums[v-offset] = nums[v-offset], v
		}
	}
	minv = 1
	for _, v := range nums {
		if v > minv {
			break
		}
		if v > 0 {
			minv++
		}
	}
	return minv
}
