package lengthoflongestsubstring

func lengthOfLongestSubstring(s string) int {
	byteLastPos := map[byte]int{}

	left := 0
	maxLen := 0
	for i := range s {
		if p, ok := byteLastPos[s[i]]; ok {
			if p >= left {
				left = p + 1
			}
		}
		if i-left+1 > maxLen {
			maxLen = i - left + 1
		}
		byteLastPos[s[i]] = i
	}
	return maxLen
}
