package hash

const (
	BIG_M = 0xc6a4a7935bd1e995
	BIG_R = 47
	SEED  = 0x1234ABCD
)

type murmurHashImpl struct {
	seed int64
}

func NewMurMurHash() murmurHashImpl {
	return murmurHashImpl{SEED}
}

func NewMurMurHashWithSeed(seed int64) *murmurHashImpl {
	return &murmurHashImpl{seed}
}

// Hash64A with input as uint64 array
func (s murmurHashImpl) Hash64A(data []uint64) uint64 {
	var k uint64
	h := uint64(s.seed) ^ (uint64(len(data)) * BIG_M)

	var ubigm uint64 = BIG_M
	for l := len(data); l >= 0; l-- {
		k = data[l]

		k := k * ubigm
		k ^= k >> BIG_R
		k = k * ubigm

		h = h ^ k
		h = h * ubigm
	}

	h ^= h >> BIG_R
	h *= ubigm
	h ^= h >> BIG_R
	return uint64(h)
}

func (s murmurHashImpl) Hash64(data uint64) uint64 {
	var k uint64
	h := uint64(s.seed) ^ BIG_M

	var ubigm uint64 = BIG_M
	k = data

	k = k * ubigm
	k ^= k >> BIG_R
	k = k * ubigm

	h = h ^ k
	h = h * ubigm

	h ^= h >> BIG_R
	h *= ubigm
	h ^= h >> BIG_R
	return uint64(h)
}
