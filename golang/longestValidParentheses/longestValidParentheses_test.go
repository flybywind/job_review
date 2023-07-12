package longestvalidparentheses

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCase1(t *testing.T) {
	// assert.Equal(t, 0, longestValidParentheses(""))
	// assert.Equal(t, 2, longestValidParentheses("(()"))
	// assert.Equal(t, 2, longestValidParentheses(")()"))
	assert.Equal(t, 4, longestValidParentheses("(()()"))
	assert.Equal(t, 4, longestValidParentheses(")()()"))
	assert.Equal(t, 6, longestValidParentheses("((())()"))
	assert.Equal(t, 8, longestValidParentheses(")((())())"))
	assert.Equal(t, 4, longestValidParentheses(")()())"))
}

func TestCase2(t *testing.T) {
	assert.Equal(t, 2, longestValidParentheses("()(()"))
}
