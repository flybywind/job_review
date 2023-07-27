package arrangerectonestrip

import "container/heap"

type Rect struct {
	count int
	idx   int
}

type RectHeap []Rect

func (r RectHeap) Len() int           { return len(r) }
func (r RectHeap) Less(i, j int) bool { return r[i].count > r[j].count }
func (r RectHeap) Swap(i, j int)      { r[i], r[j] = r[j], r[i] }
func (r *RectHeap) Push(a any)        { (*r) = append((*r), a.(Rect)) }
func (r *RectHeap) Pop() any          { a := (*r)[r.Len()-1]; (*r) = (*r)[:r.Len()-1]; return a }
func Solution(A []int, B []int) int {
	if len(A) == 1 {
		return 1
	}
	// Implement your solution here
	rectHeap := make(RectHeap, 0, 2*len(A))
	countMap := map[int]int{}
	for i, s := range A {
		rectHeap = append(rectHeap, Rect{1, i}, Rect{1, i})
		countMap[s]++
		countMap[B[i]]++
	}
	for i, s := range A {
		rectHeap[i*2].count = countMap[s]
	}
	for i, s := range B {
		rectHeap[i*2+1].count = countMap[s]
	}
	heap.Init(&rectHeap)
	cand := heap.Pop(&rectHeap).(Rect)
	minNum := cand.count / 2
	maxNum := 0
	for cand.count >= minNum && rectHeap.Len() > 0 {
		potentialCnt := cand.count
		dupNum := 0
		side1, side2 := A[cand.idx], B[cand.idx]
		for cand.count == potentialCnt {
			s1 := A[cand.idx]
			s2 := B[cand.idx]
			if !(side1 == s1 || side1 == s2 ||
				side2 == s1 || side2 == s2) {
				break
			}
			if s1 == s2 {
				dupNum++
			}
			cand = heap.Pop(&rectHeap).(Rect)
		}
		if potentialCnt-dupNum/2 > maxNum {
			maxNum = potentialCnt - dupNum/2
		}
	}
	return maxNum
}
