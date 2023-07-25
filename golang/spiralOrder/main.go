package spiralorder

var dir4 = [][2]int{{1, 0}, {0, 1}, {-1, 0}, {0, -1}}

type Cmp func(int, int) bool
type collision struct {
	cmp   Cmp
	bound int
	dim   int
}

var greater Cmp = func(a, b int) bool {
	return a >= b
}
var less Cmp = func(a, b int) bool {
	return a <= b
}

func spiralOrder(matrix [][]int) []int {
	rowN := len(matrix)
	colN := len(matrix[0])
	collisionCond := []collision{{greater, colN, 0}, {greater, rowN, 1}, {less, -1, 0}, {less, 0, 1}}

	s := 0
	total := rowN * colN
	out := make([]int, total)
	i := [2]int{0, 0}
	d := 0
	for s < total {
		cond := &collisionCond[d]
		if cond.cmp(i[cond.dim], cond.bound) {
			// switch
			i[cond.dim] -= dir4[d][cond.dim]
			cond.bound = i[cond.dim]
			d++
			d = d % 4
		} else {
			out[s] = matrix[i[1]][i[0]]
			s++
		}
		i[0] += dir4[d][0]
		i[1] += dir4[d][1]
	}
	return out
}
