package subsets

import (
	"fmt"
	"sort"
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"
)

func assertSliceAryEqual(t *testing.T, a1, a2 [][]int) bool {
	if !assert.Equal(t, len(a1), len(a2)) {
		return false
	}
	sortInter := func(a [][]int) []string {
		ret := make([]string, len(a))
		for i := range a {
			sort.IntSlice(a[i]).Sort()
			tmp := make([]string, len(a[i]))
			for j := range a[i] {
				tmp[j] = fmt.Sprintf("%d", a[i][j])
			}
			ret[i] = strings.Join(tmp, "")
		}
		sort.StringSlice(ret).Sort()
		return ret
	}
	s1 := sortInter(a1)
	s2 := sortInter(a2)
	for i := range s1 {
		if !assert.Equal(t, s1[i], s2[i]) {
			return false
		}
	}
	return true
}
func TestCase(t *testing.T) {
	a1 := [][]int{{}, {0}}
	assertSliceAryEqual(t, a1, subsets([]int{0}))
}
func TestCase1(t *testing.T) {
	a1 := [][]int{{}, {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}}
	assertSliceAryEqual(t, a1, subsets([]int{1, 2, 3}))
}

func TestCase2(t *testing.T) {
	a1 := [][]int{{}, {9}, {0}, {0, 9}, {3}, {3, 9}, {0, 3}, {0, 3, 9}, {5}, {5, 9}, {0, 5}, {0, 5, 9}, {3, 5}, {3, 5, 9}, {0, 3, 5}, {0, 3, 5, 9}, {7}, {7, 9}, {0, 7}, {0, 7, 9}, {3, 7}, {3, 7, 9}, {0, 3, 7}, {0, 3, 7, 9}, {5, 7}, {5, 7, 9}, {0, 5, 7}, {0, 5, 7, 9}, {3, 5, 7}, {3, 5, 7, 9}, {0, 3, 5, 7}, {0, 3, 5, 7, 9}}
	assertSliceAryEqual(t, a1, subsets([]int{9, 0, 3, 5, 7}))
}
