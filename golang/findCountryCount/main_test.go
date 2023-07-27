package findcountrycount

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCase1(t *testing.T) {
	assert.Equal(t, 11, Solution([][]int{
		{5, 4, 4},
		{4, 3, 4},
		{3, 2, 4},
		{2, 2, 2},
		{3, 3, 4},
		{1, 4, 4},
		{4, 1, 1}}))
}
