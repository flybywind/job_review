package subsets

import (
	"math"
)

func _inter_(nums []int, ret [][]int) [][]int {
	if len(nums) == 1 {
		ret = append(ret, []int{nums[0]})
		return ret
	}
	ret = _inter_(nums[1:], ret)
	for i := range ret {
		j := len(ret[i])
		// must use full lenght slice, to force copy of the ret[i], or it'll re-use the
		// same underlying array, which may cause error
		ret = append(ret, append(ret[i][:j:j], nums[0]))
	}
	return ret
}
func subsets(nums []int) [][]int {
	n := len(nums)
	if n == 0 {
		return [][]int{}
	}
	ret := make([][]int, 0, int(math.Pow(2, float64(n))))
	ret = append(ret, []int{})
	return _inter_(nums, ret)
}
