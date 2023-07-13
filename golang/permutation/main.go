package permutation

import "math"

func insert2(s string, b byte, p int) string {
	if p == 0 {
		return string(b) + s
	}
	if p >= len(s) {
		return s + string(b)
	}
	return s[:p] + string(b) + s[p:]
}
func permutation(s string) []string {
	if len(s) == 1 {
		return []string{s}
	}
	if len(s) == 2 {
		if s[0] != s[1] {
			return []string{s, s[1:] + s[:1]}
		} else {
			return []string{s}
		}
	}
	p2 := permutation(s[1:])
	res := make([]string, 0, len(s)*len(p2))
	for i := 0; i < len(p2); i++ {
		// find next valid p
		var last_char byte = math.MaxInt8
		for p := 0; p < len(p2[i]); p++ {
			if last_char != s[0] {
				res = append(res, insert2(p2[i], s[0], p))
			}
			last_char = p2[i][p]
		}
		if last_char != s[0] {
			res = append(res, insert2(p2[i], s[0], len(p2[i])))
		}
	}
	return res
}
