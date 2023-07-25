package partitionlabels

func partitionLabels(s string) []int {
	charMap := map[byte][]int{}
	for i := range s {
		b := s[i]
		if _, ok := charMap[b]; ok {
			charMap[b][1] = i + 1
		} else {
			charMap[b] = []int{i, i + 1}
		}
	}
	procChar := map[byte]struct{}{}
	ret := make([]int, 0, 3)
	for i := 0; i < len(s); i++ {
		b := s[i]
		procChar[b] = struct{}{}
		span := charMap[b]
		ovst, ovend, ovsum := -1, -1, 0 // overlap start/end
		left := 0
		for j, ll := range ret {
			right := left + ll
			if span[0] >= left && span[1] <= right {
				// already discovered
				goto LOOP
			}
			if (span[0] >= left && span[0] < right) ||
				(span[1] >= left && span[1] < right) ||
				(left >= span[0] && left < span[1]) {
				//overlap
				if ovst == -1 {
					ovst = j
					ovend = j
					ovsum = ret[j]
				} else {
					ovend = j
					ovsum += ret[j]
				}
			} else {
				if ovend > ovst && ovst >= 0 {
					break
				}
			}
			left = right
		}
		if ovst >= 0 {
			if ovend+1 < len(ret) {
				ret = append(append(ret[:ovst], ovsum), ret[ovend+1:]...)
			} else {
				if left < span[1] {
					ovsum += (span[1] - left)
				}
				ret = append(ret[:ovst], ovsum)
			}
		} else {
			ret = append(ret, (span[1] - span[0]))
		}

	LOOP:
	}
	return ret
}

// 事实上只看每个字符的最大下标就可以了。判断一个区间是否结束，只要看是否遍历到 end 下标即可 s
// func partitionLabels(s string) (partition []int) {
//     lastPos := [26]int{}
//     for i, c := range s {
//         lastPos[c-'a'] = i
//     }
//     start, end := 0, 0
//     for i, c := range s {
//         if lastPos[c-'a'] > end {
//             end = lastPos[c-'a']
//         }
//         if i == end {
//             partition = append(partition, end-start+1)
//             start = end + 1
//         }
//     }
//     return
// }

// 作者：LeetCode-Solution
// 链接：https://leetcode.cn/problems/partition-labels/solution/hua-fen-zi-mu-qu-jian-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
