package firstmissingpositive

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCase1(t *testing.T) {
	assert.Equal(t, 3, firstMissingPositive([]int{1, 2, 0}))
	assert.Equal(t, 2, firstMissingPositive([]int{4, 3, -1, 1}))
	assert.Equal(t, 1, firstMissingPositive([]int{4, 3, 2, 2, 5}))
}

func TestCase2(t *testing.T) {
	assert.Equal(t, 3, firstMissingPositive([]int{1, 2, 100}))
	assert.Equal(t, 2, firstMissingPositive([]int{4, 3, -1, 1, 100}))
}

func TestCase3(t *testing.T) {
	assert.Equal(t, 2, firstMissingPositive([]int{1, -1, 1}))
}
