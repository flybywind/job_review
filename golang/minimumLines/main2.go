package minimumlines

import "math"

type bitSet struct {
	data []uint8
	num  int
	size int // non-zero bits num
}

func createBitSet(bitNum int) bitSet {
	n := int(math.Log(float64(bitNum))/math.Log(8.0)) + 1
	return bitSet{data: make([]uint8, n), num: bitNum}
}

func (s *bitSet) set(p int) {
	if s.get(p) {
		return
	}
	n := p / 8
	m := p % 8
	s.data[n] |= (uint8(1) << m)
	s.size++
}
func (s *bitSet) clear(p int) {
	if !s.get(p) {
		return
	}
	n := p / 8
	m := p % 8
	s.data[n] &= (^(uint8(1) << m))
	s.size--
}
func (s bitSet) get(p int) bool {
	n := p / 8
	m := p % 8
	return (s.data[n] & (uint8(1) << m)) > 0
}

type line struct {
	a, b, c float32
}

func floatEqal(a, b float32, eps float32) bool {
	d := a - b
	if d < 0 {
		d = -d
	}
	return d < eps
}
func (l line) lieAt(p []int) bool {
	return floatEqal(l.a*float32(p[0])+l.b*float32(p[1]), l.c, 1e-8)
}

func from2point(p1, p2 []int) *line {
	x1, y1 := p1[0], p1[1]
	x2, y2 := p2[0], p2[1]
	l := &line{}
	if x1 != x2 {
		l.a = float32(y2-y1) / float32(x1-x2)
		l.b = 1
		l.c = float32(x1*y2-x2*y1) / float32(x1-x2)
	} else {
		l.a = 1
		l.b = 0
		l.c = float32(x1)
	}

	return l
}

func minimumLines(points [][]int) int {
	pNum := len(points)
	if pNum <= 2 {
		return 1
	}
	minLino := pNum
	var innerFunc func([][]int, bitSet, int) int
	innerFunc = func(points [][]int, bs bitSet, d int) int {
		if d >= minLino {
			return 1
		}
		leftNum := len(points) - bs.size
		if leftNum <= 2 {
			return 1
		}
		curMin := pNum
		for i, p := range points {
			if bs.get(i) {
				continue
			}
			bs.set(i)
			for j := 0; j < pNum; j++ {
				if j == i {
					continue
				}
				p2 := points[j]
				bs.set(j)
				l := from2point(p, p2)
				for k := 0; k < pNum; k++ {
					if bs.get(k) {
						continue
					}
					p3 := points[k]
					if l.lieAt(p3) {
						bs.set(k)
					}
				}

				bs2 := createBitSet(pNum)
				copy(bs2.data, bs.data)
				bs2.size = bs.size
				lino := innerFunc(points, bs2, d+1)
				if lino < curMin {
					curMin = lino
				}
			}
		}
		if minLino < curMin+1 {
			minLino = curMin + 1
		}
		return curMin + 1
	}

	bs := createBitSet(pNum)
	innerFunc(points, bs, 0)
	return minLino
}
