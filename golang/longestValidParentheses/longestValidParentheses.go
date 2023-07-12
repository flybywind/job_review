package longestvalidparentheses

// use FILO stack

type stack []int

func (s *stack) Push(p int) {
	*s = append(*s, p)
}
func (s stack) Empty() bool {
	return len(s) == 0
}
func (s *stack) Pop() int {
	a := *s
	*s = a[:len(a)-1]
	return a[len(a)-1]
}

func longestValidParenthesesMy(seq string) int {
	if len(seq) <= 1 {
		return 0
	}
	stk := stack{}
	col_ary := make([]int, len(seq))
	for i, b := range seq {
		if b == ')' {
			if !stk.Empty() {
				col_ary[stk.Pop()] = 1
				col_ary[i] = 1
			}
			continue
		}
		//b == '('
		stk.Push(i)
	}
	longest_val_len := 0
	longest_val_start := 0
	if col_ary[0] == 1 {
		longest_val_start = 0
	}
	for i := 1; i < len(col_ary); i++ {
		if col_ary[i-1] != 1 && col_ary[i] == 1 {
			longest_val_start = i
		}
		if col_ary[i] != 1 && col_ary[i-1] == 1 {
			ln := i - longest_val_start
			if ln > longest_val_len {
				longest_val_len = ln
			}
		}
		if i == len(col_ary)-1 && col_ary[i] == 1 {
			ln := i + 1 - longest_val_start
			if ln > longest_val_len {
				longest_val_len = ln
			}
		}
	}
	return longest_val_len
}

// LeeCode solution
// 链接：https://leetcode.cn/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
func longestValidParentheses(s string) int {
	maxAns := 0
	stack := []int{}
	// 这里其实保存了2类信息，一个是所有左括号下标，二是未匹配的右括号下标
	// 未匹配的右括号下标是通过判断pop后，stack是否为空来获取的。再就是在初始化的时候，
	// 通过赋值为-1，表示那个不存在的位置。这样就大大简化了长度的计算逻辑
	stack = append(stack, -1)
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			stack = append(stack, i)
		} else {
			stack = stack[:len(stack)-1]
			if len(stack) == 0 {
				stack = append(stack, i)
			} else {
				maxAns = max(maxAns, i-stack[len(stack)-1])
			}
		}
	}
	return maxAns
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
