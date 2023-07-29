package equaldigitfrequency

import "fmt"

func equalDigitFrequency(s string) int {
	N := len(s)
	uniqSeq := map[string]struct{}{}
	for i := 0; i < N; i++ {
		charCount := [10]int{}
		maxCount := 1
		totalCount := 1
		charCount[int(s[i]-'0')] = 1
		for j := i + 1; j <= N; j++ {
			if (j-i)%totalCount == 0 && (j-i)/totalCount == maxCount {
				fmt.Printf("[%d, %d] %s\n", i, j, s[i:j])
				uniqSeq[s[i:j]] = struct{}{}
			}
			if j < N {
				idx := int(s[j] - '0')
				if charCount[idx] == 0 {
					totalCount++
				}
				charCount[idx] += 1
				if charCount[idx] > maxCount {
					maxCount = charCount[idx]
				}
			}
		}
	}
	return len(uniqSeq)
}
