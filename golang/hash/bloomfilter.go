package hash

import (
	"math"
	"math/rand"
)

type Hash interface {
	Hash64A(data []byte) uint64
}
type BloomFilter struct {
	data    []uint64
	filters []Hash
	k       int    // hash func size
	m       uint64 // bits num
	rndGen  *rand.Rand
	buf     []byte
}

func NewBloomFilter(size int, tol float32, seed int64) *BloomFilter {
	a := float64(size) * math.Log2(float64(tol)) / math.Log(2)
	m := uint64(math.Ceil(-a))
	n := m>>6 + 1
	k := -int(math.Ceil(math.Log2(float64(tol))))
	bf := BloomFilter{
		m:    uint64(m),
		k:    k,
		data: make([]uint64, n),
		buf:  make([]byte, 8),
	}

	bf.filters = make([]Hash, k)
	bf.rndGen = rand.New(rand.NewSource(seed))
	for i := range bf.filters {
		bf.filters[i] = NewMurMurHashWithSeed(bf.rndGen.Int63())
	}
	return &bf
}

func (bf *BloomFilter) Set(e int64) {
	b := &bf.buf
	// a := make([]byte, 8)
	// b := &a
	bf.trans(e, *b)
	for i, f := range bf.filters {
		bf.setbit((f.Hash64A(*b) + uint64(i*i)) % bf.m)
	}
}
func (bf *BloomFilter) trans(e int64, bits []byte) {
	for i := 0; i < len(bits); i++ {
		bits[i] = byte(e & 0xff)
		e >>= 8
	}
}
func (bf *BloomFilter) setbit(m uint64) {
	i := m >> 6
	j := m & 0x3f
	bf.data[i] |= (1 << j)
}
func (bf *BloomFilter) testbit(m uint64) bool {
	i := m >> 6
	j := m & 0x3f
	return (bf.data[i] & (1 << j)) > 0
}
func (bf *BloomFilter) Hit(e int64) bool {
	b := &bf.buf
	// a := make([]byte, 8)
	// b := &a
	bf.trans(e, *b)
	for i, f := range bf.filters {
		if !bf.testbit((f.Hash64A(*b) + uint64(i*i)) % bf.m) {
			return false
		}
	}
	return true
}
