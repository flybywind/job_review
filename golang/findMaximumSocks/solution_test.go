package findmaximumsocks

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCase1(t *testing.T) {
	assert.Equal(t, 3, Solution(2, []int{1, 2, 1, 1}, []int{1, 4, 3, 2, 4}))
}

func TestCase2(t *testing.T) {
	assert.Equal(t, 3, Solution(2, []int{1, 2, 3, 1}, []int{1, 4, 3, 2, 4}))
	assert.Equal(t, 1, Solution(0, []int{1, 2, 3, 1}, []int{1, 4, 3, 2, 4}))
}

func TestCase3(t *testing.T) {
	assert.Equal(t, 4, Solution(4, []int{1, 2, 3, 1}, []int{1, 4, 3, 2, 4}))
}
