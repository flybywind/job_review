package golang

type Stack []int

func (s *Stack) Pop() (int, bool) {

	if len(*s) == 0 {
		return -1, false
	}
	p := (*s)[s.Len()-1]
	*s = (*s)[:(s.Len() - 1)]
	return p, true
}

func (s *Stack) Push(p int) {
	*s = append(*s, p)
}

func (s Stack) IsEmpty() bool {
	return len(s) == 0
}

func (s Stack) Len() int {
	return len(s)
}

func reverseStackRecursive(s Stack) {
	if s.Len() < 2 {
		return
	}
	var popK func(*Stack, int) (int, bool)
	popK = func(s *Stack, k int) (int, bool) {
		if k == 0 || s.IsEmpty() {
			return -1, false
		}
		p, _ := s.Pop()
		if ret, ok := popK(s, k-1); ok {
			s.Push(p)
			return ret, true
		} else {
			if k > 1 {
				return -1, false
			}
			return p, true
		}
	}
	for k := 2; k <= s.Len(); k++ {
		p, ok := popK(&s, k)
		if ok {
			s.Push(p)
		} else {
			return
		}
	}
}
