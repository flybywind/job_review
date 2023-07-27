package minimumlines

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCase1(t *testing.T) {
	assert.Equal(t, 2, minimumLines([][]int{{0, 1}, {2, 3}, {4, 5}, {4, 3}}))
}

func TestCase2(t *testing.T) {
	assert.Equal(t, 1, minimumLines([][]int{{0, 2}, {-2, -2}, {1, 4}}))
}

func TestCase3(t *testing.T) {
	// random fail
	assert.Equal(t, 3, minimumLines([][]int{{0, 0}, {-5, 0}, {4, -2}, {3, -2}, {4, 2}, {1, -2}, {-2, -1}, {5, 0}}))
}
