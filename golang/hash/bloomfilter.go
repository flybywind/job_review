package hash

import (
	"math"
	"math/rand"
)

type BloomFilter struct {
	data    []uint64
	filters []*murmurHashImpl
	k       int    // hash func size
	m       uint64 // bits num
	rndGen  *rand.Rand
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
	}

	bf.filters = make([]*murmurHashImpl, k)
	bf.rndGen = rand.New(rand.NewSource(seed))
	for i := range bf.filters {
		bf.filters[i] = NewMurMurHashWithSeed(bf.rndGen.Int63())
	}
	return &bf
}

func (bf *BloomFilter) Set(e uint64) {
	for i, f := range bf.filters {
		bf.setbit((f.Hash64(e) + uint64(i*i)) % bf.m)
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
func (bf *BloomFilter) Hit(e uint64) bool {
	for i, f := range bf.filters {
		if !bf.testbit((f.Hash64(e) + uint64(i*i)) % bf.m) {
			return false
		}
	}
	return true
}
