package singlenonduplicate

func _iter_inner(nums []int, left, right int) int {
	if right-left == 1 {
		return nums[left]
	}
	mid := (left + right) / 2
	if nums[mid] != nums[mid-1] && nums[mid] != nums[mid+1] {
		return nums[mid]
	}
	if nums[mid] == nums[mid-1] {
		if (mid-left)%2 == 0 { // even number go same direction
			return _iter_inner(nums, left, mid-1)
		} else {
			return _iter_inner(nums, mid+1, right)
		}
	}
	// nums[mid] == nums[mid+1]
	if (mid-left)%2 == 0 { // even number go same direction
		return _iter_inner(nums, mid+2, right)
	} else {
		return _iter_inner(nums, left, mid)
	}

}

func singleNonDuplicate(nums []int) int {
	return _iter_inner(nums, 0, len(nums))
}
