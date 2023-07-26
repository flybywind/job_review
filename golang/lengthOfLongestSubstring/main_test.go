package lengthoflongestsubstring

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCase1(t *testing.T) {
	assert.Equal(t, 3, lengthOfLongestSubstring("abcabcbb"))
}

func TestCase2(t *testing.T) {
	assert.Equal(t, 1, lengthOfLongestSubstring("bbbbb"))
}

func TestCase3(t *testing.T) {
	assert.Equal(t, 3, lengthOfLongestSubstring("pwwkew"))
}

func TestCase4(t *testing.T) {
	assert.Equal(t, 2, lengthOfLongestSubstring("aab"))
}

func TestCase5(t *testing.T) {
	assert.Equal(t, 5, lengthOfLongestSubstring("tmmzuxt"))
}
