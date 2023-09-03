package golang

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	n1 := len(nums1)
	n2 := len(nums2)
	isEven := (n1+n2)%2 == 0

	var recursiveFind func(nums1 []int, nums2 []int, pos int) float64
	recursiveFind = func(nums1 []int, nums2 []int, pos int) float64 {
		n1 := len(nums1)
		n2 := len(nums2)
		if n1 == 0 || n2 == 0 {
			if n1 > 0 {
				nums1 = nums1[:pos]
				n1 = pos
			} else {
				nums2 = nums2[:pos]
				n2 = pos
			}
		}
		if pos == (n1 + n2) {
			i, j := n1-1, n2-1
			temp := make([]int, 0, 2)
			for len(temp) < 2 {
				if i >= 0 && j >= 0 {
					if nums1[i] > nums2[j] {
						temp = append(temp, nums1[i])
						i--
					} else {
						temp = append(temp, nums2[j])
						j--
					}
				} else {
					if i >= 0 {
						temp = append(temp, nums1[i])
						i--
					} else if j >= 0 {
						temp = append(temp, nums2[j])
						j--
					} else {
						break
					}
				}
			}
			if isEven {
				return float64(temp[0]+temp[1]) / 2.0
			}
			return float64(temp[0])
		}

		r := float32(pos) / float32(n1+n2)
		p1 := int32(float32(n1) * r)
		p2 := int32(float32(n2) * r)
		if nums1[p1] > nums2[p2] {
			return recursiveFind(nums1[:p1], nums2, pos)
		} else {
			return recursiveFind(nums1, nums2[:p2], pos)
		}
	}

	return recursiveFind(nums1, nums2, (n1+n2)/2+1)
}

// brute force version
func findMedianSortedArrays_BF(nums1 []int, nums2 []int) float64 {
	n1, n2 := len(nums1), len(nums2)
	mid := (n1+n2)/2 + 1
	var ret, ret0 int
	for i, j, n := 0, 0, 0; n < mid; n++ {
		ret0 = ret
		if i < n1 && j < n2 {
			if nums1[i] < nums2[j] {
				ret = nums1[i]
				i++
			} else {
				ret = nums2[j]
				j++
			}
		} else {
			if i < n1 {
				ret = nums1[i]
				i++
			} else if j < n2 {
				ret = nums2[j]
				j++
			}
		}
	}
	if (n1+n2)%2 == 0 {
		return float64(ret+ret0) / 2
	}
	return float64(ret)
}
