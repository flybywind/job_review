package singlenonduplicate

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCase1(t *testing.T) {
	assert.Equal(t, 2, singleNonDuplicate([]int{1, 1, 2, 3, 3, 4, 4, 8, 8}))
	assert.Equal(t, 10, singleNonDuplicate([]int{3, 3, 7, 7, 10, 11, 11}))
}
