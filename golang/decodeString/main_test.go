package decodestring

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCase1(t *testing.T) {
	for _, test := range []struct {
		input  string
		expect string
	}{
		{
			"3[a]2[bc]",
			"aaabcbc",
		},
		{
			"a2[c]",
			"acc",
		},
		{
			"3[a2[c]]",
			"accaccacc",
		},
		{
			"2[abc]3[cd]ef",
			"abcabccdcdcdef",
		},
		{
			"abc3[cd]xyz",
			"abccdcdcdxyz",
		},
	} {
		name := test.input + "exp: " + test.expect
		output := decodeString(test.input)
		assert.Equal(t, test.expect, output, name)
	}
}
