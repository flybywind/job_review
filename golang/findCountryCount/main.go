package findcountrycount

// you can also use imports, for example:
// import "fmt"
// import "os"

// you can write to stdout for debugging purposes, e.g.
// fmt.Println("this is a debug message")

type point struct {
	r, c int
}

func Solution(A [][]int) int {
	// Implement your solution here
	countryIdx := 0
	rowNum := len(A)
	colNum := len(A[0])
	markMap := make([][]bool, rowNum)
	for j := 0; j < rowNum; j++ {
		markMap[j] = make([]bool, colNum)
	}
	dir4 := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	iterateMap := func(r, c int, color int) {
		candidates := []point{{r, c}}
		for len(candidates) > 0 {
			curp := candidates[len(candidates)-1]
			candidates = candidates[:len(candidates)-1]
			r, c := curp.r, curp.c
			for _, d := range dir4 {
				r2, c2 := r+d[0], c+d[1]
				if r2 >= 0 && r2 < rowNum &&
					c2 >= 0 && c2 < colNum &&
					A[r2][c2] == color {
					if !markMap[r2][c2] {
						markMap[r2][c2] = true
						candidates = append(candidates, point{r2, c2})
					}
				}
			}
		}
	}
	for i := 0; i < rowNum; i++ {
		for j := 0; j < colNum; j++ {
			if !markMap[i][j] {
				countryIdx++
				markMap[i][j] = true
				iterateMap(i, j, A[i][j])
			}
		}
	}
	return countryIdx
}
