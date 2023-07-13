package permutation

import (
	"fmt"
	"sort"
	"testing"

	"github.com/stretchr/testify/assert"
)

func assertStrEqual(t *testing.T, s1, s2 []string) {
	if !assert.Equal(t, len(s1), len(s2)) {
		return
	}
	sort.StringSlice(s1).Sort()
	sort.StringSlice(s2).Sort()
	for i := range s1 {
		assert.Equal(t, fmt.Sprintf("%d: %s", i, s1[i]), fmt.Sprintf("%d: %s", i, s2[i]))
	}
}

func TestCase1(t *testing.T) {
	assertStrEqual(t, []string{"abc", "acb", "bac", "bca", "cab", "cba"}, permutation("abc"))
}

func TestCase2(t *testing.T) {
	assertStrEqual(t, []string{"aba", "aab", "baa"}, permutation("aab"))
}
