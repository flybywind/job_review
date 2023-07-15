package reorderlist

/**
 * Definition for singly-linked list.
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

func reorderList(head *ListNode) {
	var n int
	curn := head
	for curn != nil {
		n++
		curn = curn.Next
	}
	if n < 3 {
		return
	}

	curn = head
	var stackn, nextn *ListNode
	var i, m int = 0, n / 2
	for curn != nil {
		nextn = curn.Next
		if i >= m {
			curn.Next = stackn
			stackn = curn
		}
		curn = nextn
		i++
	}
	curn = head
	for stackn != nil {
		if curn.Next == stackn || curn == stackn {
			stackn.Next = nil
			break
		}
		curn, curn.Next = curn.Next, stackn
		stackn, stackn.Next = stackn.Next, curn
	}
}
