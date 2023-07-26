package addtwonumbers

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCase1(t *testing.T) {
	assert.Equal(t, "7,0,8", addTwoNumbers(FromArray([]int{2, 4, 3}), FromArray([]int{5, 6, 4})).Repr())
}

func TestCase2(t *testing.T) {
	assert.Equal(t, "0", addTwoNumbers(FromArray([]int{0}), FromArray([]int{0})).Repr())
}

func TestCase3(t *testing.T) {
	assert.Equal(t, "8,9,9,9,0,0,0,1", addTwoNumbers(FromArray([]int{9, 9, 9, 9, 9, 9, 9}), FromArray([]int{9, 9, 9, 9})).Repr())
}
