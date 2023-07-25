package nextgreaterelements

// 一个简短的栈就把这个问题解决了。。。
// 还是要从简单的思路出发，思路就是，如果我们找到了元素，它如果比
// 前面的元素大，那么它肯定是符合条件的nextGreaterElement，
// 而前面比它小的元素都可以算作成功找出answser，没有找到ans的下标
// 继续入栈，同时继续遍历nums数组。相当于2个指针，一个顺着下标找，
// 一个逆着下标找(从栈顶到底的寻找)
func nextGreaterElements(nums []int) []int {
	n := len(nums)
	ans := make([]int, n)
	for i := range ans {
		ans[i] = -1
	}
	stack := []int{}
	for i := 0; i < n*2-1; i++ {
		for len(stack) > 0 && nums[stack[len(stack)-1]] < nums[i%n] {
			ans[stack[len(stack)-1]] = nums[i%n]
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, i%n)
	}
	return ans

	// 作者：LeetCode-Solution
	// 链接：https://leetcode.cn/problems/next-greater-element-ii/solution/xia-yi-ge-geng-da-yuan-su-ii-by-leetcode-bwam/
	// 来源：力扣（LeetCode）
	// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
}
