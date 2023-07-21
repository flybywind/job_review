package effortlesspath

import (
	"container/heap"
	"fmt"
	"math"
)

type point struct{ x, y, minEffort int }
type hp []point

func (h hp) Len() int           { return len(h) }
func (h hp) Less(i, j int) bool { return h[i].minEffort < h[j].minEffort }
func (h hp) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v any)        { *h = append(*h, v.(point)) }
func (h *hp) Pop() any          { a := *h; *h = a[:len(a)-1]; return a[len(a)-1] }

type step struct{ x, y int }

var dir4 = []step{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

func minimumEffortPath(heights [][]int) int {
	rowN := len(heights)
	if rowN == 0 {
		return 0
	}
	colN := len(heights[0])
	if colN == 0 {
		return 0
	}
	effortHeap := &hp{{0, 0, 0}}
	minEffort := 0
	sptSet := map[[2]int]struct{}{}
	for effortHeap.Len() > 0 {
		p := heap.Pop(effortHeap).(point)
		sptSet[[2]int{p.x, p.y}] = struct{}{}
		if p.x == colN-1 && p.y == rowN-1 {
			minEffort = p.minEffort
			break
		}
		for _, d := range dir4 {
			x, y := p.x+d.x, p.y+d.y
			if x >= colN || x < 0 ||
				y >= rowN || y < 0 {
				// skip
				continue
			}
			if _, ok := sptSet[[2]int{x, y}]; ok {
				// already calculated, skip
				fmt.Println("skip", x, y)
				continue
			}
			effort := max(p.minEffort, abs(heights[y][x]-heights[p.y][p.x]))
			p2 := point{x, y, effort}
			heap.Push(effortHeap, p2)
		}
	}
	return minEffort
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func abs(x int) int {
	if x < 0 {
		if x == math.MinInt {
			return math.MaxInt
		}
		return -x
	}
	return x
}
