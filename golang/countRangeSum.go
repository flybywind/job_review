package golang

func countRangeSum(nums []int, lower int, upper int) int {
	N := len(nums)
	sums := make([]int64, N)
	s := int64(0)
	for i := 0; i < N; i++ {
		s += int64(nums[i])
		sums[i] = s
	}

	var div_concur func(sums []int64, left, right int) int
	div_concur = func(sums []int64, left int, right int) int {
		N := right - left
		if N == 1 {
			if sums[left] >= int64(lower) && sums[left] <= int64(upper) {
				return 1
			}
			return 0
		}
		mid := (left + right) / 2
		cl := div_concur(sums, left, mid)
		cr := div_concur(sums, mid, right)

		cm := 0
		i1, i2 := left, left
		for j := mid; j < right; j++ {
			e := sums[j]
			lower2 := e - int64(upper)
			upper2 := e - int64(lower)
			for ; i1 < mid && sums[i1] < lower2; i1++ {
			} // until sums[i1] >= lower2
			if i1 >= mid {
				break
			}
			i2 = i1
			for ; i2 < mid && sums[i2] <= upper2; i2++ {
			} // untile sums[i2] > upper2
			cm += (i2 - i1)
		}
		i := left
		j := mid
		tmp := make([]int64, 0, right-left)
		for i < mid && j < right {
			if sums[i] <= sums[j] {
				tmp = append(tmp, sums[i])
				i++
			} else {
				tmp = append(tmp, sums[j])
				j++
			}
		}
		for ; i < mid; i++ {
			tmp = append(tmp, sums[i])
		}
		for ; j < right; j++ {
			tmp = append(tmp, sums[j])
		}
		for i = left; i < right; i++ {
			sums[i] = tmp[i-left]
		}
		return cl + cr + cm
	}
	return div_concur(sums, 0, N)
}

func countRangeSumBruteForce(nums []int, lower int, upper int) int {
	N := len(nums)
	c := 0
	for i := 0; i < N; i++ {
		sum := int64(0)
		for j := i; j < N; j++ {
			sum += int64(nums[j])
			if sum >= int64(lower) && sum <= int64(upper) {
				c++
			}
		}
	}
	return c
}
