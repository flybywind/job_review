package atmostngivendigitset

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCase(t *testing.T) {
	assert.Equal(t, 1, atMostNGivenDigitSet([]string{"7"}, 8))
	assert.Equal(t, 2, atMostNGivenDigitSet([]string{"1", "3", "5", "7"}, 3))
}
func TestCase1(t *testing.T) {
	assert.Equal(t, 20, atMostNGivenDigitSet([]string{"1", "3", "5", "7"}, 100))
}

func TestCase2(t *testing.T) {
	assert.Equal(t, 29523, atMostNGivenDigitSet([]string{"1", "4", "9"}, 1000000000))
}

func TestCase3(t *testing.T) {
	// assert.Equal(t, 47, atMostNGivenDigitSet([]string{"1", "3", "5", "7"}, 256))
	assert.Equal(t, 10, atMostNGivenDigitSet([]string{"1", "7"}, 231))
}

func TestCase4(t *testing.T) {
	assert.Equal(t, 6, atMostNGivenDigitSet([]string{"5", "7", "8"}, 59))
}

func TestCase5(t *testing.T) {
	assert.Equal(t, 3, atMostNGivenDigitSet([]string{"1"}, 834))
}

func TestCase6(t *testing.T) {
	assert.Equal(t, 79, atMostNGivenDigitSet([]string{"1", "2", "3", "6", "7", "8"}, 211))
}

func TestCase7(t *testing.T) {
	assert.Equal(t, 59979, atMostNGivenDigitSet([]string{"1", "2", "3", "4", "5", "6", "7", "8", "9"}, 91243))
}
