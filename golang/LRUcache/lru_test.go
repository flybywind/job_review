package lrucache

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestLRU_queue(t *testing.T) {
	q := NewDLinkQueue(3)
	assert.Equal(t, 0, q.size)
	q.PushFront(&Node{Val: "abc"})
	assert.Equal(t, 1, q.size)
	q.PushFront(&Node{Val: "123"})
	assert.Equal(t, 2, q.size)
	n := q.PopEnd()
	assert.Equal(t, "abc", n.Val)
	assert.Equal(t, 1, q.size)
	n = &Node{Val: "4"}
	q.PushFront(n)
	q.PushFront(&Node{Val: "5"}) // "5" -> "4" -> "123"
	assert.Equal(t, "5", n.prev.Val)
	assert.Equal(t, "123", n.next.Val)
	assert.Equal(t, "4", n.Val)
	q.PopNode(n) // // "5" -> "123"
	assert.Equal(t, (*Node)(nil), n.prev)
	assert.Equal(t, (*Node)(nil), n.next)
	assert.Equal(t, 2, q.size)
	n = q.tail.prev
	assert.Equal(t, "123", n.Val)
	assert.Equal(t, "5", n.prev.Val)
}

func TestLRU_cap(t *testing.T) {
	q := NewDLinkQueue(3)
	q.PushFront(&Node{Val: "abc"})
	q.PushFront(&Node{Val: "123"})
	q.PushFront(&Node{Val: "4"})
	q.PushFront(&Node{Val: "5"}) // "5" -> "4" -> "123" -> nil ("abc" was evicted)

	assert.Equal(t, 3, q.size)
	n := q.tail.prev
	assert.Equal(t, "123", n.Val)
}

func TestLRU_cache(t *testing.T) {
	cache := NewLRUCache(3)
	cache.Put(1, "a")
	cache.Put(2, "b")
	cache.Put(3, "c")
	val, exist := cache.Get(1)
	assert.Equal(t, true, exist)
	assert.Equal(t, "a", val)
	val, exist = cache.Get(2)
	assert.Equal(t, true, exist)
	assert.Equal(t, "b", val)
	val, exist = cache.Get(3)
	assert.Equal(t, true, exist)
	assert.Equal(t, "c", val)
}

func TestLRU_cache_replacevalue(t *testing.T) {
	cache := NewLRUCache(3)
	cache.Put(1, "a")
	cache.Put(2, "b")
	cache.Put(3, "c")
	cache.Put(1, "d")
	val, exist := cache.Get(1)
	assert.Equal(t, true, exist)
	assert.Equal(t, "d", val)
}

func TestLRU_cache_evictold(t *testing.T) {
	cache := NewLRUCache(3)
	cache.Put(1, "a")
	cache.Put(2, "b")
	cache.Put(3, "c")
	cache.Put(4, "d")
	val, exist := cache.Get(1)
	assert.Equal(t, false, exist)
	val, exist = cache.Get(2)
	assert.Equal(t, true, exist)
	assert.Equal(t, "b", val)
	val, exist = cache.Get(4)
	assert.Equal(t, true, exist)
	assert.Equal(t, "d", val)
}