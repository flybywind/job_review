package atmostngivendigitset

import (
	"math"
	"sort"
	"strconv"
)

func getDecBits(n int) []string {
	ret := make([]string, 0, int(math.Log10(float64(n))+1))
	for n > 0 {
		ret = append(ret, strconv.FormatInt(int64(n%10), 10))
		n = n / 10
	}
	return ret
}
func numOflessThan(digits []string, v string) int {
	return sort.SearchStrings(digits, v)
}
func atMostNGivenDigitSet(digits []string, n int) int {
	dn := len(digits)
	sum := 0
	m := 1
	decbit := getDecBits(n)
	multCache := make([]int, 0, len(decbit)+1)
	multCache = append(multCache, 1)
	for i := 0; i < len(decbit)-1; i++ {
		m = m * dn
		multCache = append(multCache, m)
		sum += m
	}

	lastNum := ""
	for i := len(decbit) - 1; i >= 0; i-- {
		// case ["1"], 856
		if i > 0 && lastNum != "" && lastNum < decbit[i-1] {
			break
		}
		lessnum := numOflessThan(digits, decbit[i])
		if i == 0 && lessnum < len(digits) &&
			digits[lessnum] == decbit[i] {
			lessnum++
		}
		if lessnum < 1 { // case [ "1", "3", "4"] 125
			if digits[lessnum] == decbit[i] {
				continue
			} else {
				break
			}
		}
		sum += lessnum * multCache[i]
		if lessnum < len(digits) {
			lastNum = digits[lessnum]
		} else {
			lastNum = digits[len(digits)-1]
		}
	}
	return sum
}
