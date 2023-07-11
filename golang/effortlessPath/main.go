package effortlesspath

import (
	"math"
)

func max(vals ...int) int {
	r := math.MinInt
	for _, v := range vals {
		if v > r {
			r = v
		}
	}
	return r
}
func min(vals ...int) int {
	r := math.MaxInt
	for _, v := range vals {
		if v < r {
			r = v
		}
	}
	return r
}
func abs(v int) int {
	if v >= 0 {
		return v
	}
	if v < 0 {
		if v == math.MinInt {
			return math.MaxInt
		}
		return -v
	}
	return 0
}

func minimumEffortPath(heights [][]int) int {
	rowN := len(heights)
	if rowN == 0 {
		return 0
	}
	colN := len(heights[0])
	if colN == 0 {
		return 0
	}

	energyMat := make([][]int, rowN)
	for i := 0; i < rowN; i++ {
		energyMat[i] = make([]int, colN)
	}
	col := 0

	for i := 1; i < rowN; i++ {
		energyMat[i][col] = max(energyMat[i-1][col], abs(heights[i][col]-heights[i-1][col]))
	}

	row := 0
	for i := 1; i < colN; i++ {
		energyMat[row][i] = max(energyMat[row][i-1], abs(heights[row][i]-heights[row][i-1]))
	}

	for i := 1; i < rowN; i++ {
		for j := 1; j < colN; j++ {
			energyMat[i][j] = min(
				max(energyMat[i][j-1], abs(heights[i][j-1]-heights[i][j])), // left ->
				max(energyMat[i-1][j], abs(heights[i-1][j]-heights[i][j]))) // top ->
		}
	}
	return energyMat[rowN-1][colN-1]
}
