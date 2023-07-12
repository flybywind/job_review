package maxprofit

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCase1(t *testing.T) {
	assert.Equal(t, 5, maxProfit([]int{7, 1, 5, 3, 6, 4}))
	assert.Equal(t, 0, maxProfit([]int{7, 6, 5, 4, 3, 2}))
	assert.Equal(t, 3, maxProfit([]int{6, 7, 2, 5, 4, 3, 2, 1}))
}
