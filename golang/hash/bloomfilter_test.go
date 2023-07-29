package hash

import (
	"fmt"
	"math/rand"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestBloomFilter(t *testing.T) {
	seed := int64(12345678)
	bf := NewBloomFilter(5000, 0.01, seed)
	rndGen := rand.New(rand.NewSource(seed))
	insertVals := map[uint64]bool{}
	for i := 0; i < 6_000; i++ {
		r := uint64(rndGen.Int63n(10_000-1) + 1)
		// t.Log("insert", r, "at", i)
		insertVals[r] = true
		bf.Set(r)
	}

	fp_count := 0
	tn_count := 0
	for i := uint64(0); i < 10_000; i++ {
		// if bloom filter return false, then this element must not has been inserted
		if !bf.Hit(i) {
			if !assert.Equal(t, false, insertVals[i]) {
				t.Log("failed at", i)
				return
			}
			tn_count++
		}
		// check the false positive rate:
		if bf.Hit(i) && !insertVals[i] {
			fp_count++
		}
	}
	fmt.Printf("false negative rate: %f, true negative count: %d\n", float64(fp_count)/float64(10_0000), tn_count)
	assert.LessOrEqual(t, float64(fp_count)/float64(10_0000), 1e-3)
}

func BenchmarkBloomFilter(b *testing.B) {
	seed := int64(12345678)
	bf := NewBloomFilter(5000, 0.1, seed)
	rndGen := rand.New(rand.NewSource(seed))
	for i := 0; i < 5_000; i++ {
		r := uint64(rndGen.Int63n(10_000-1) + 1)
		// t.Log("insert", r, "at", i)
		bf.Set(r)
	}
	tn_count := 0
	b.ResetTimer()
	for n := 0; n < b.N; n++ {
		for i := uint64(0); i < 10_000; i++ {
			// if bloom filter return false, then this element must not has been inserted
			if !bf.Hit(i) {
				tn_count++
			}
		}
	}
	b.Log(tn_count)
}

func BenchmarkHashMap(b *testing.B) {
	seed := int64(12345678)
	hashMap := map[int64]bool{}
	rndGen := rand.New(rand.NewSource(seed))
	for i := 0; i < 5_000; i++ {
		r := rndGen.Int63n(10_000-1) + 1
		hashMap[r] = true
	}
	tn_count := 0
	b.ResetTimer()
	for n := 0; n < b.N; n++ {
		for i := int64(0); i < 10_000; i++ {
			// if bloom filter return false, then this element must not has been inserted
			if !hashMap[i] {
				tn_count++
			}
		}
	}
	b.Log(tn_count)
}
