package golang

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestReverserStackRecursive(t *testing.T) {
	t.Run("test1", func(t *testing.T) {
		ary := []int{0, 1, 2, 3, 4, 5}
		stk := Stack(ary)
		reverseStackRecursive(stk)

		assert.Equal(t, 6, stk.Len())
		assert.Equal(t, 5, ary[0])
		assert.Equal(t, 4, ary[1])
		assert.Equal(t, 3, ary[2])
		assert.Equal(t, 2, ary[3])
		assert.Equal(t, 1, ary[4])
		assert.Equal(t, 0, ary[5])
	})
}
