package minimalksum

import (
	"container/heap"
	"sort"
)

type IntHeap struct {
	sort.IntSlice
}

func (h *IntHeap) Push(a any) { h.IntSlice = append(h.IntSlice, a.(int)) }
func (h *IntHeap) Pop() any {
	a := h.IntSlice[h.Len()-1]
	h.IntSlice = h.IntSlice[:h.Len()-1]
	return a
}

func minimalKSum(nums []int, k int) int64 {
	h := &IntHeap{sort.IntSlice(nums)}
	heap.Init(h)

	sumn := int64(0)
	n := 0
	prev := 0
	var cur int
	for h.Len() > 0 {
		cur = heap.Pop(h).(int)
		if cur > prev+1 {
			for i := prev + 1; i < cur; i++ {
				sumn += int64(i)
				n++
				if n >= k {
					return sumn
				}
			}
		}
		prev = cur
	}
	for n < k {
		sumn += int64(cur) + 1
		cur++
		n++
	}
	return sumn
}
