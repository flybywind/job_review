package minimalksum

import (
	"math/rand"
	"testing"

	"github.com/stretchr/testify/assert"
)

func forceSolution(nums []int, k int) int64 {
	numMap := map[int64]struct{}{}
	for _, n := range nums {
		numMap[int64(n)] = struct{}{}
	}
	sumn := int64(0)
	for i, n := int64(1), 0; n < k; i++ {
		if _, ok := numMap[i]; !ok {
			sumn += i
			n++
		}
	}
	return sumn
}

func TestCase1(t *testing.T) {
	nums := []int{1, 4, 25, 10, 25}
	assert.Equal(t, int64(5), forceSolution(nums, 2))
	assert.Equal(t, int64(5), minimalKSum(nums, 2))
}

func TestCase2(t *testing.T) {
	nums := []int{5, 6}
	assert.Equal(t, int64(25), forceSolution(nums, 6))
	assert.Equal(t, int64(25), minimalKSum(nums, 6))
}

func TestBloomFilter(t *testing.T) {
	seed := int64(12345678)
	bf := NewBloomFilter(5000, 0.01, seed)
	rndGen := rand.New(rand.NewSource(seed))
	insertVals := map[int64]bool{}
	for i := 0; i < 5_000; i++ {
		r := rndGen.Int63n(10_000-1) + 1
		// t.Log("insert", r, "at", i)
		insertVals[r] = true
		bf.Set(r)
	}

	fp_count := 0
	tn_count := 0
	for i := int64(0); i < 10_000; i++ {
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
	t.Log("false negative rate:", fp_count, "true negative count:", tn_count)
	assert.LessOrEqual(t, float64(fp_count)/float64(10_0000), 1e-3)
}

func BenchmarkBloomFilter(b *testing.B) {
	seed := int64(12345678)
	bf := NewBloomFilter(5000, 0.1, seed)
	rndGen := rand.New(rand.NewSource(seed))
	for i := 0; i < 5_000; i++ {
		r := rndGen.Int63n(10_000-1) + 1
		// t.Log("insert", r, "at", i)
		bf.Set(r)
	}
	tn_count := 0
	b.ResetTimer()
	for n := 0; n < b.N; n++ {
		for i := int64(0); i < 10_000; i++ {
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
