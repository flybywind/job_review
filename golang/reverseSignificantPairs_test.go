package golang

import (
	"math/rand"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestReversePair(t *testing.T) {
	N := 20
	R := 5
	nums := make([]int, N)
	rnd := rand.New(rand.NewSource(12345))
	for r := 0; r < R; r++ {
		for i := 0; i < N; i++ {
			nums[i] = rnd.Intn(50)
		}
		expect := reversePairsBruteForce(nums)
		t.Logf("pair num: %d, nums = %v\n", expect, nums)
		assert.Equal(t, expect, reversePairs(nums))
	}
}

func TestReversePair0(t *testing.T) {
	nums := []int{0}
	assert.Equal(t, 0, reversePairs(nums))
	nums = []int{}
	assert.Equal(t, 0, reversePairs(nums))
}

func TestReversePairNegNum(t *testing.T) {
	// nums := []int{-5, -5}
	// assert.Equal(t, 1, reversePairs(nums))

	nums := []int{3, -6, 0, 1, 1, 0, -5, 5, -5, -3}
	assert.Equal(t, 29, reversePairs(nums))
}

func TestReversePairNegRand(t *testing.T) {
	N := 10
	R := 5
	nums := make([]int, N)
	rnd := rand.New(rand.NewSource(12345))
	for r := 0; r < R; r++ {
		for i := 0; i < N; i++ {
			nums[i] = rnd.Intn(10) - rnd.Intn(10)
		}
		expect := reversePairsBruteForce(nums)
		t.Logf("pair num: %d, nums = %v\n", expect, nums)
		assert.Equal(t, expect, reversePairs(nums))
	}
}
