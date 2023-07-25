package nextgreaterelements

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func arrayEqual(t *testing.T, ary1, ary2 []int) bool {
	if !assert.Equal(t, len(ary1), len(ary2)) {
		return false
	}
	return assert.Equal(t, ary1, ary2)
}
func TestCase1(t *testing.T) {
	arrayEqual(t, []int{2, -1, 2}, nextGreaterElements([]int{1, 2, 1}))
}

func TestCase2(t *testing.T) {
	arrayEqual(t, []int{2, 3, 4, -1, 4}, nextGreaterElements([]int{1, 2, 3, 4, 3}))
}

func TestCase3(t *testing.T) {
	arrayEqual(t, []int{2, 4, 2, 2, 4, -1, 4}, nextGreaterElements([]int{1, 2, 1, 1, 2, 4, 3}))
}

func TestCase4(t *testing.T) {
	arrayEqual(t, []int{-1, 5, 5, 5, 5}, nextGreaterElements([]int{5, 4, 3, 2, 1}))
}
