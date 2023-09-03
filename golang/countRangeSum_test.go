package golang

import (
	"math/rand"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCaseRandomNum(t *testing.T) {
	N := 10
	R := 5
	nums := make([]int, N)
	scale := 10
	rnd := rand.New(rand.NewSource(12345))
	for r := 0; r < R; r++ {
		for i := 0; i < N; i++ {
			nums[i] = rnd.Intn(scale) - rnd.Intn(scale)
		}
		lower := rnd.Intn(scale*2) - rnd.Intn(scale*2)
		upper := rnd.Intn(scale*2) - rnd.Intn(scale*2)
		if lower > upper {
			lower, upper = upper, lower
		}
		expect := countRangeSumBruteForce(nums, lower, upper)
		t.Logf("range sum num: %d, nums = %v, range [%d, %d]\n", expect, nums, lower, upper)
		assert.Equal(t, expect, countRangeSum(nums, lower, upper))
	}
}
func TestCase1(t *testing.T) {
	nums := []int{3, 6, 3, -2, 8, 1, 3, 3, 4, 1}
	lower, upper := -3, 2
	assert.Equal(t, 4, countRangeSum(nums, lower, upper))
}

func TestCase2(t *testing.T) {
	nums := []int{-2, -6, -4, -5, -3, -7, -3, 1, 2, 1}
	lower, upper := -7, -5
	assert.Equal(t, 5, countRangeSum(nums, lower, upper))
}

func TestCase3(t *testing.T) {
	nums := []int{3, 6, 4, 1, -1, -4, 3, -6, 0, 1}
	lower, upper := 1, 10
	assert.Equal(t, 22, countRangeSum(nums, lower, upper))
}
