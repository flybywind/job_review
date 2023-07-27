package maxsumafteronesquare

import "math"

// "container/heap"

// type node struct {
// 	source, current int
// 	is2             bool
// 	sum             int
// }
// type pathHeap []node

// func (h pathHeap) Less(i, j int) bool { return h[i].sum < h[j].sum }
// func (h pathHeap) Len() int           { return len(h) }
// func (h *pathHeap) Push(a any)        { *h = append(*h, a.(node)) }
// func (h *pathHeap) Pop() any          { a := (*h)[h.Len()-1]; *h = (*h)[:h.Len()-1]; return a }
// func (h pathHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func maxSumAfterOperation(nums []int) int {
	N := len(nums)
	if N == 1 {
		return nums[0] * nums[0]
	}
	nums2 := make([]int, N)
	for i, v := range nums {
		nums2[i] = v * v
	}
	for j := N - 2; j >= 0; j-- {
		v := nums[j]
		nums[j] = v + max(0, nums[j+1])

		nums2[j] = max(nums2[j]+max(0, nums[j+1]), v+nums2[j+1])
	}
	maxSum := math.MinInt
	for _, v := range nums2 {
		if v > maxSum {
			maxSum = v
		}
	}
	return maxSum
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
