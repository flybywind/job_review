package frog_jump

import (
	"fmt"
	"math"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestFrogJump(t *testing.T) {
	assert.Equal(t, 3, numWays(3))
	assert.Equal(t, 21, numWays(7))
	assert.Equal(t, 720754435, numWays(92))
}

func TestIntMax(t *testing.T) {
	t.Log("max int64 =", math.MaxInt64)
	t.Log("len of max int64 =", len(fmt.Sprintf("%d", math.MaxInt64)))
}
