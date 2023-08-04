package inversenode

type Node struct {
	Val  int
	Next *Node
}

func InverseLink(r *Node) *Node {
	var prev *Node = nil
	cur := r
	for cur.Next != nil {
		next := cur.Next
		cur.Next = prev
		prev = cur
		cur = next
	}
	return cur
}

func InverseLinkRecursive(cur, prev *Node) *Node {
	if cur.Next == nil {
		return cur
	}
	cur.Next = prev
	return InverseLinkRecursive(cur.Next, cur)
}
