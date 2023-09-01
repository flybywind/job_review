package golang

func _div_concur(nums []int, left, right int) int {
	if right-left == 1 {
		return 0
	}
	if right-left == 2 {
		ret := 0
		if nums[left] >= nums[right-1] {
			if nums[left] > 2*nums[right-1] {
				ret = 1
			}
			nums[left], nums[right-1] = nums[right-1], nums[left]
		}
		return ret
	}
	mid := (left + right) / 2
	countLeft := _div_concur(nums, left, mid)
	countRight := _div_concur(nums, mid, right)

	middleCount := 0

	temp := make([]int, 0, right-left)

	i := left
	j := mid
	ii := i
	for i < mid && j < right {
		if nums[i] >= nums[j] {
			if nums[i] > 2*nums[j] {
				middleCount += (mid - i)
			} else {
				if ii < i {
					ii = i
				}
				for ii < mid && nums[ii] <= 2*nums[j] {
					ii++
				}
				middleCount += (mid - ii)
			}
			temp = append(temp, nums[j])
			j++
		} else {
			temp = append(temp, nums[i])
			i++
		}
	}
	for i < mid {
		temp = append(temp, nums[i])
		i++
	}
	for j < right {
		temp = append(temp, nums[j])
		j++
	}
	for k := left; k < right; k++ {
		nums[k] = temp[k-left]
	}
	return countLeft + countRight + middleCount
}
func reversePairs(nums []int) int {
	if len(nums) <= 1 {
		return 0
	}
	return _div_concur(nums, 0, len(nums))
}

func reversePairsBruteForce(nums []int) int {
	N := len(nums)
	if N <= 1 {
		return 0
	}
	ret := 0
	for i := 0; i < N; i++ {
		for j := i + 1; j < N; j++ {
			if nums[i] > 2*nums[j] {
				ret++
			}
		}
	}
	return ret
}
