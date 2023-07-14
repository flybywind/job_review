package subarraysum

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCase(t *testing.T) {
	assert.Equal(t, 2, subarraySum([]int{1, 1, 1}, 2))
	assert.Equal(t, 2, subarraySum([]int{1, 2, 3}, 3))
	assert.Equal(t, 0, subarraySum([]int{1}, 0))
}

func TestCase1(t *testing.T) {
	assert.Equal(t, 3, subarraySum([]int{1, -1, 0}, 0))
}
