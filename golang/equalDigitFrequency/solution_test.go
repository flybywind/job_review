package equaldigitfrequency

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCase1(t *testing.T) {
	assert.Equal(t, 5, equalDigitFrequency("1212"))
}

func TestCase2(t *testing.T) {
	assert.Equal(t, 9, equalDigitFrequency("12321"))
}

func TestCase3(t *testing.T) {
	assert.Equal(t, 14, equalDigitFrequency("12123321"))
	// 1, 2, 12,
}
