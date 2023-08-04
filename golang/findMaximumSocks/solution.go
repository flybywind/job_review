package findmaximumsocks

import "sort"

// you can also use imports, for example:
// import "fmt"
// import "os"

// you can write to stdout for debugging purposes, e.g.
// fmt.Println("this is a debug message")

type SockInfo struct {
	color int
	dirty bool
}
type SockList []SockInfo

func (s SockList) Len() int      { return len(s) }
func (s SockList) Swap(i, j int) { s[i], s[j] = s[j], s[i] }
func (s SockList) Less(i, j int) bool {
	if s[i].color < s[j].color {
		return true
	} else if s[i].color == s[j].color {
		return !s[i].dirty
	}
	return false
}
func Solution(K int, C []int, D []int) int {
	// Implement your solution here
	slst := SockList{}
	for _, s := range C {
		slst = append(slst, SockInfo{s, false})
	}
	for _, s := range D {
		slst = append(slst, SockInfo{s, true})
	}

	sort.Sort(slst)
	sn := len(slst)
	leftK := K
	curp := 0
	leftSocks := []*SockInfo{}
	for i := 0; i+1 < sn; {
		if slst[i].color != slst[i+1].color {
			i++
			continue
		}
		if !slst[i].dirty && !slst[i+1].dirty {
			curp++
		} else if !slst[i].dirty && slst[i+1].dirty {
			if leftK > 0 {
				// laundry it
				leftK--
				curp++
			}
		} else {
			leftSocks = append(leftSocks, &slst[i], &slst[i+1])
		}
		i += 2
	}
	if len(leftSocks) >= 2 && leftK >= 2 {
		for i := 0; i+1 < len(leftSocks) && leftK >= 2; {
			if leftSocks[i].color == leftSocks[i+1].color {
				curp++
				leftK -= 2
				i += 2
				continue
			}
			i++
		}
	}
	return curp
}
