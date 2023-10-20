package lrucache

type Node struct {
	Val string
	key int
	prev, next *Node
}

type dlinkQueue struct {
	head, tail *Node
	size int
	cap int
}

func NewDLinkQueue(cap int) *dlinkQueue {
	q := &dlinkQueue{
		size: 0,
		cap: cap,
	}
	
	q.head = &Node{ }
	q.tail = &Node{ }
	q.head.next = q.tail
	q.tail.prev = q.head
	return q
}

// func (q *dlinkQueue) PopFront() *Node {
// 	if q.size == 0 {
// 		return nil
// 	}
// 	ret := q.head.next
// 	q.head.next = ret.next
// 	ret.next.prev = q.head
// 	ret.next = nil
// 	ret.prev = nil
// 	q.size --
// 	return ret
// }

func (q *dlinkQueue) PopEnd() *Node {
	if q.size == 0 {
		return nil
	}
	ret := q.tail.prev
	q.PopNode(ret)	
	return ret
}

func (q *dlinkQueue) PopNode(n *Node) {
	prev := n.prev
	next := n.next
	n.prev = nil
	n.next = nil
	prev.next = next
	next.prev = prev
	q.size --
}

func (q *dlinkQueue) PushFront(n *Node) *Node{
	first := q.head.next
	q.head.next = n
	n.prev = q.head
	n.next = first
	first.prev = n 
	q.size ++
	if q.size > q.cap {
		return q.PopEnd()
	}
	return nil
}

type LRUcache struct {
	q *dlinkQueue
	m map[int]*Node
}

func NewLRUCache(cap int) *LRUcache {
	ret := &LRUcache{
		q: NewDLinkQueue(cap),
		m: map[int]*Node{},
	}
	return ret
}

func (c *LRUcache) Put(key int, val string) {
	if n, ok := c.m[key]; ok {
		c.q.PopNode(n)	
		c.q.PushFront(n)
		n.Val = val
		// c.m[key] = n
	} else {
		n := &Node{Val: val, key: key}
		poped := c.q.PushFront(n)
		c.m[key] = n
		if poped != nil {
			delete(c.m, poped.key)
		}
	}
}

func (c * LRUcache) Get(key int) (val string, exist bool) {
	if n, ok := c.m[key]; ok {
		val = n.Val
		c.q.PopNode(n)
		c.q.PushFront(n)
		return val, true
	} else {
		return "", false
	}
}