package effortlesspath

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCase1(t *testing.T) {
	heights := [][]int{{1, 2, 2}, {3, 8, 2}, {5, 3, 5}}
	assert.Equal(t, 2, minimumEffortPath(heights))
}

func TestCase2(t *testing.T) {
	heights := [][]int{{1, 2, 3}, {3, 8, 4}, {5, 3, 5}}
	assert.Equal(t, 1, minimumEffortPath(heights))
}

func TestCase3(t *testing.T) {
	heights := [][]int{{1, 2, 1, 1, 1}, {1, 2, 1, 2, 1}, {1, 2, 1, 2, 1}, {1, 2, 1, 2, 1}, {1, 1, 1, 2, 1}}
	assert.Equal(t, 0, minimumEffortPath(heights))
}
