package robber

func rob0(nums []int) int {
	n := len(nums)
	var robSum, robMax int
	for i := 0; n-i >= n/2; i++ {
		robMark := make([]int, n)
		robSum = 0

		for j := i; j < n; j += 2 {
			if j+1 == n && robMark[0] == 1 {
				continue
			}

			robSum += nums[j]
			robMark[j] = 1
		}
		if robSum > robMax {
			robMax = robSum
		}
	}
	return robMax
}

func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func _rob_innter(nums []int, sumMat [][]int, p, n int) int {
	if n-p <= 0 {
		return 0
	}
	if n-p == 1 {
		sumMat[p][n] = nums[p]
		return nums[p]
	}
	if sumMat[p][n] >= 0 {
		return sumMat[p][n]
	}
	var s, maxRob, left, right int
	for i := p; i < n; i++ {
		left = i - 1
		right = i + 1
		if left < p {
			left = n
		}
		if right >= n {
			right = p - 1
		}
		if left < right {
			sumMat[i][n] = _rob_innter(nums, sumMat, i, i+1) + _rob_innter(nums, sumMat, right+1, n)
			s = _rob_innter(nums, sumMat, p, left) + sumMat[i][n]
		} else {
			s = _rob_innter(nums, sumMat, right+1, left) + _rob_innter(nums, sumMat, i, i+1)
		}
		if s > maxRob {
			maxRob = s
		}
	}
	sumMat[p][n] = maxRob
	return maxRob
}
func rob(nums []int) int {
	n := len(nums)
	if n < 2 {
		return 0
	}
	sumMat := make([][]int, n)
	for i := 0; i < n; i++ {
		sumMat[i] = make([]int, n+1)
		for j := 0; j < n+1; j++ {
			sumMat[i][j] = -1
		}
	}
	maxrob := 0
	// 这明显可以转变成动态规划问题啊。。。。
	// exclude first house
	_rob_innter(nums, sumMat, 1, n)
	// include first house
	_rob_innter(nums, sumMat, 0, n-1)
	sumMat[0][n] = sumMat[0][n-1]
	for i := 0; i < n; i++ {
		r := sumMat[i][n]
		if r > maxrob {
			maxrob = r
		}
	}
	return maxrob
}
