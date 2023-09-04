package main

import "fmt"

type Board struct {
	n        int   // N x N
	queenPos []int //
}

func CreateBoard(n int) *Board {
	return &Board{
		n:        n,
		queenPos: make([]int, n),
	}
}

func (b *Board) NQueen(verbos int) int {
	var sol int = 0
	var recurFunc func(q int, bitmap []int64)
	recurFunc = func(q int, bitmap0 []int64) {
		bitmap := append([]int64{}, bitmap0...)
		bit := bitmap[q]
		if bit == ((1 << b.n) - 1) {
			return
		}
		for i := 0; i < b.n; i++ {
			if bit&(1<<i) == 0 {
				b.queenPos[q] = i
				if q == b.n-1 {
					sol++
					if verbos > 1 {
						fmt.Println("find solution:", sol)
						b.Print()
					}
					continue
				}
				// update following bits
				for j, step := q+1, 1; j < b.n; j++ {
					bitmap[j] |= (1 << i)
					if i-step >= 0 {
						bitmap[j] |= (1 << (i - step))
					}
					if i+step < b.n {
						bitmap[j] |= (1 << (i + step))
					}
					step++
				}
				recurFunc(q+1, bitmap)
				// reset the bitmap
				bitmap = append([]int64{}, bitmap0...)
			}
		}
	}
	bitmap := make([]int64, b.n)
	recurFunc(0, bitmap)
	return sol
}

func (b Board) Print() {
	for i := 0; i < b.n; i++ {
		for j := 0; j < b.n; j++ {
			if b.queenPos[i] == j {
				fmt.Print(" * ")
			} else {
				fmt.Print(" 0 ")
			}
		}
		fmt.Println()
	}
}

func main() {
	verbos := 2
	N := 1
	b := CreateBoard(N)

	fmt.Println("N =", N, "total solutions =", b.NQueen(verbos))

	N = 2
	b = CreateBoard(N)

	fmt.Println("N =", N, "total solutions =", b.NQueen(verbos))

	N = 3
	b = CreateBoard(N)

	fmt.Println("N =", N, "total solutions =", b.NQueen(verbos))

	N = 4
	b = CreateBoard(N)

	fmt.Println("N =", N, "total solutions =", b.NQueen(verbos))

	N = 5
	b = CreateBoard(N)

	fmt.Println("N =", N, "total solutions =", b.NQueen(verbos))

	N = 6
	b = CreateBoard(N)

	fmt.Println("N =", N, "total solutions =", b.NQueen(verbos))

	for n := 7; n < 15; n++ {
		N = n
		b = CreateBoard(N)
		fmt.Println("N =", N, "total solutions =", b.NQueen(1))
	}

}
