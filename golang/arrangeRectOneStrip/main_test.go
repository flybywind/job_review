package arrangerectonestrip

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCase1(t *testing.T) {
	assert.Equal(t, 3, Solution([]int{2, 3, 2, 3, 5}, []int{3, 4, 2, 4, 2}))
}
