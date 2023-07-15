package reorderlist

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func CreateLink(nums []int) *ListNode {
	var root *ListNode = &ListNode{nums[0], nil}
	var curn *ListNode = root
	for i := 1; i < len(nums); i++ {
		curn.Next = &ListNode{nums[i], nil}
		curn = curn.Next
	}
	return root
}

func assertLinkEqual(t *testing.T, l1, l2 *ListNode) bool {
	for l1 != nil && l2 != nil {
		if !assert.Equal(t, l1.Val, l2.Val) {
			return false
		}
		l1 = l1.Next
		l2 = l2.Next
	}
	return assert.Equal(t, l1, l2)
}
func TestCase1(t *testing.T) {
	origLink := CreateLink([]int{1, 2, 3, 4})
	reorderList(origLink)
	link2 := CreateLink([]int{1, 4, 2, 3})
	assertLinkEqual(t, link2, origLink)
}

func TestCase2(t *testing.T) {
	origLink := CreateLink([]int{1, 2, 3, 4, 5})
	reorderList(origLink)
	link2 := CreateLink([]int{1, 5, 2, 4, 3})
	assertLinkEqual(t, link2, origLink)
}
