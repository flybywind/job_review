package maxsumafteronesquare

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCase1(t *testing.T) {
	assert.Equal(t, 17, maxSumAfterOperation([]int{2, -1, -4, -3}))
}

func TestCase2(t *testing.T) {
	assert.Equal(t, 4, maxSumAfterOperation([]int{1, -1, 1, 1, -1, -1, 1}))
}
