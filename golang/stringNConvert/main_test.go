package stringnconvert

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCase1(t *testing.T) {
	var s = "PAYPALISHIRING"
	assert.Equal(t, "PAHNAPLSIIGYIR", convert(s, 3))
}

func TestCase2(t *testing.T) {
	var s = "PAYPALISHIRING"
	assert.Equal(t, "PINALSIGYAHRPI", convert(s, 4))
}

func TestCase0(t *testing.T) {
	var s = "A"
	assert.Equal(t, "A", convert(s, 1))
	assert.Equal(t, "A", convert(s, 2))
}
