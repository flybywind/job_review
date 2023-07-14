package subarraysum

// 枚举法，只能实现o(n2)的复杂度
func subarraySum(nums []int, k int) int {
	if len(nums) == 0 {
		return 0
	}
	var p, q, n, sum int

	for q = 0; q < len(nums); q++ {
		if q > 0 {
			for sum > k && p < q {
				// move ahead p til sum  <= k
				sum -= nums[p]
				p++
			}
			if sum == k {
				n++
			}
		}
		sum += nums[q]
	}
	// for i := p; i < len(nums); i++ {
	// 	if sum == k {
	// 		n++
	// 	}
	// 	sum -= nums[i]
	// }
	// if sum == k {
	// 	n++
	// }
	return n
}

// 作者：LeetCode-Solution
// 链接：https://leetcode.cn/problems/QTMn0o/solution/he-wei-k-de-zi-shu-zu-by-leetcode-soluti-1169/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
// 可以这么考虑，
// pre[i] = sum[0-i](nums[i])
// 那么，以i结尾的，从前面某个位置j开始的位置，和为k的j，满足条件是
//
//	pre[j] = pre[i] - k
//
// 我们只需要知道j的数量即可。那么我们可以用sum[0-j]即pre[j]为key，
// 因为nums里面的元素都只能是int，所以可以考虑用map进行预处理，出现的次数为value，构建这样的map
func subarraySum2(nums []int, k int) int {
	count, pre := 0, 0
	m := map[int]int{}
	m[0] = 1
	for i := 0; i < len(nums); i++ {
		pre += nums[i]
		if _, ok := m[pre-k]; ok {
			count += m[pre-k]
		}
		m[pre] += 1
	}
	return count
}
