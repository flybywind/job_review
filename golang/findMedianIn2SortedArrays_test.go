package golang

import (
	"math/rand"
	"sort"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestFindMedianSortedArrays(t *testing.T) {
	t.Run("test1", func(t *testing.T) {
		nums1 := []int{0, 1, 3, 6}
		nums2 := []int{2, 4, 8} // 0 1 2 3 4 6 8
		assert.Equal(t, 3.0, findMedianSortedArrays_BF(nums1, nums2))
		nums1 = []int{0, 1, 2, 4}
		nums2 = []int{3, 8, 10} // 0 1 2 3 4 8 10
		assert.Equal(t, 3.0, findMedianSortedArrays_BF(nums1, nums2))
		nums1 = []int{0, 1}
		nums2 = []int{2, 3, 4, 8, 10} // 0 1 2 3 4 8 10
		assert.Equal(t, 3.0, findMedianSortedArrays_BF(nums1, nums2))
		nums1 = []int{0}
		nums2 = []int{1, 2, 3, 4, 8, 10} // 0 1 2 3 4 8 10
		assert.Equal(t, 3.0, findMedianSortedArrays_BF(nums1, nums2))
	})
	t.Run("test2", func(t *testing.T) {
		nums1 := []int{0, 1, 3, 6}
		nums2 := []int{2, 4, 8} // 0 1 2 3 4 6 8
		assert.Equal(t, 3.0, findMedianSortedArrays(nums1, nums2))
		nums1 = []int{0, 1, 2, 4}
		nums2 = []int{3, 8, 10} // 0 1 2 3 4 8 10
		assert.Equal(t, 3.0, findMedianSortedArrays(nums1, nums2))
		nums1 = []int{0, 1}
		nums2 = []int{2, 3, 4, 8, 10} // 0 1 2 3 4 8 10
		assert.Equal(t, 3.0, findMedianSortedArrays(nums1, nums2))
		nums1 = []int{0}
		nums2 = []int{1, 2, 3, 4, 8, 10} // 0 1 2 3 4 8 10
		assert.Equal(t, 3.0, findMedianSortedArrays(nums1, nums2))
	})
	t.Run("testOneEmpty", func(t *testing.T) {
		nums1 := []int{}
		nums2 := []int{1, 2, 4, 8}
		assert.Equal(t, 3.0, findMedianSortedArrays(nums1, nums2))
	})
	t.Run("testRandomArray", func(t *testing.T) {
		seed := rand.NewSource(12789)
		rnd := rand.New(seed)

		for i := 0; i < 10; i++ {
			n1 := rnd.Intn(20) + 1
			n2 := rnd.Intn(20) + 1
			nums1 := make([]int, n1)
			nums2 := make([]int, n2)
			for j := 0; j < n1; j++ {
				nums1[j] = rnd.Intn(100) - rnd.Intn(100)
			}
			for j := 0; j < n2; j++ {
				nums2[j] = rnd.Intn(100) - rnd.Intn(100)
			}
			sort.Ints(nums1)
			sort.Ints(nums2)

			expected := findMedianSortedArrays_BF(nums1, nums2)
			t.Logf("medium of %v and %v is %f\n", nums1, nums2, expected)
			assert.Equal(t, expected, findMedianSortedArrays(nums1, nums2))
		}
	})
}
