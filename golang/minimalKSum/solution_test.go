package minimalksum

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func forceSolution(nums []int, k int) int64 {
	numMap := map[int64]struct{}{}
	for _, n := range nums {
		numMap[int64(n)] = struct{}{}
	}
	sumn := int64(0)
	for i, n := int64(1), 0; n < k; i++ {
		if _, ok := numMap[i]; !ok {
			sumn += i
			n++
		}
	}
	return sumn
}

func TestCase1(t *testing.T) {
	nums := []int{1, 4, 25, 10, 25}
	assert.Equal(t, int64(5), forceSolution(nums, 2))
	assert.Equal(t, int64(5), minimalKSum(nums, 2))
}

func TestCase2(t *testing.T) {
	nums := []int{5, 6}
	assert.Equal(t, int64(25), forceSolution(nums, 6))
	assert.Equal(t, int64(25), minimalKSum(nums, 6))
}
