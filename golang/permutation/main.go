package permutation

import (
	"math"
	"sort"
)

func insert2(s string, b byte, p int) string {
	if p == 0 {
		return string(b) + s
	}
	if p >= len(s) {
		return s + string(b)
	}
	return s[:p] + string(b) + s[p:]
}
func permutation(s string) []string {
	if len(s) == 1 {
		return []string{s}
	}
	if len(s) == 2 {
		if s[0] != s[1] {
			return []string{s, s[1:] + s[:1]}
		} else {
			return []string{s}
		}
	}
	p2 := permutation(s[1:])
	res := make([]string, 0, len(s)*len(p2))
	for i := 0; i < len(p2); i++ {
		// find next valid p
		var last_char byte = math.MaxInt8
		for p := 0; p < len(p2[i]); p++ {
			if last_char != s[0] {
				res = append(res, insert2(p2[i], s[0], p))
			}
			last_char = p2[i][p]
		}
		if last_char != s[0] {
			res = append(res, insert2(p2[i], s[0], len(p2[i])))
		}
	}
	return res
}

// backtrace回溯法和我Line30-31的思路有点像。只是在回溯法中，完美的解决了重复问题。而在我这边却没有。
// 两种不同的思路确实产生了不一样的效果。
func permutation2(s string) (ans []string) {
	t := []byte(s)
	sort.Slice(t, func(i, j int) bool { return t[i] < t[j] })
	n := len(t)
	perm := make([]byte, 0, n)
	vis := make([]bool, n)
	var backtrack func(int)
	backtrack = func(i int) {
		if i == n {
			ans = append(ans, string(perm))
			return
		}
		for j, b := range vis {
			// b == true, 当前位对应的元素已经被填充了, 跳过返回继续寻找下一个
			// or, 看下如果j > 0, 第i-1位是否被填充了，如果是，说明这一位没有
			// 被填充，继续下一步，填充该元素；
			// or,               第i-1位没有被填充，但是它好上一位相同，也直接跳过
			if b || j > 0 && !vis[j-1] && t[j-1] == t[j] {
				continue
			}
			vis[j] = true
			perm = append(perm, t[j])
			backtrack(i + 1)
			perm = perm[:len(perm)-1]
			vis[j] = false
		}
	}
	backtrack(0)
	return
}

// 作者：LeetCode-Solution
// 链接：https://leetcode.cn/problems/zi-fu-chuan-de-pai-lie-lcof/solution/zi-fu-chuan-de-pai-lie-by-leetcode-solut-hhvs/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
