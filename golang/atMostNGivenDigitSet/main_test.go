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
	assert.Equal(t, 47, atMostNGivenDigitSet([]string{"1", "3", "5", "7"}, 256))
}

func TestCase4(t *testing.T) {
	assert.Equal(t, 6, atMostNGivenDigitSet([]string{"5", "7", "8"}, 59))
}

func TestCase5(t *testing.T) {
	assert.Equal(t, 3, atMostNGivenDigitSet([]string{"1"}, 834))
}
