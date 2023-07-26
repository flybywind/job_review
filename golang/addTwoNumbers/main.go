package addtwonumbers

import (
	"strconv"
	"strings"
)

/**
 * Definition for singly-linked list.
 **/
type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	carry := 0
	sum := 0
	ret := &ListNode{}
	cur := ret
	for !(l1 == nil && l2 == nil) {
		v1, v2 := 0, 0
		if l1 != nil {
			v1 = l1.Val
		}
		if l2 != nil {
			v2 = l2.Val
		}
		sum = v1 + v2 + carry
		carry = sum / 10
		cur.Next = &ListNode{sum % 10, nil}
		cur = cur.Next
		if l2 != nil {
			l2 = l2.Next
		}
		if l1 != nil {
			l1 = l1.Next
		}
	}
	if carry > 0 {
		cur.Next = &ListNode{carry, nil}
	}
	return ret.Next
}

func (n *ListNode) Repr() string {
	ret := []string{}
	for n != nil {
		ret = append(ret, strconv.FormatInt(int64(n.Val), 10))
		n = n.Next
	}
	return strings.Join(ret, ",")
}

func FromArray(inp []int) *ListNode {
	ret := &ListNode{inp[0], nil}
	cur := ret
	for i := 1; i < len(inp); i++ {
		cur.Next = &ListNode{inp[i], nil}
		cur = cur.Next
	}
	return ret
}
