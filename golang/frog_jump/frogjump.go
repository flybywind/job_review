/*
 https://leetcode.cn/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/?envType=study-plan-v2&envId=coding-interviews
 if we define: f(n) = f(n-1) + f(n-2), then we need 2^n calculation
  need cache result
  also need to pay attenion at the value overflow
*/

package frog_jump

type fibo struct {
	cache map[int]int
}

// GetCache suitable for repeat calculation
func (f *fibo) GetCache(n int) int {
	if n == 0 || n == 1 {
		return 1
	}
	if v, ok := f.cache[n]; ok {
		return v
	}
	ret := f.Get(n-1) + f.Get(n-2)
	if ret > 1000000007 {
		ret = ret % 1000000007
	}
	f.cache[n] = ret
	return ret
}

// Get suitable for one-off calculation
func (f *fibo) Get(n int) int {
	/**
	    1, 1, 2, 3
		0, 1, 2, 3
	*/
	f0 := 1
	f1 := 1
	for i := 2; i <= n; i++ {
		f1 = f0 + f1
		f0 = f1 - f0 // f0 = previous f1
		if f1 > 1000000007 {
			f1 = f1 % 1000000007
		}
	}
	return f1
}

var f = fibo{cache: map[int]int{}}

func numWays(n int) int {
	return f.Get(n)
}
