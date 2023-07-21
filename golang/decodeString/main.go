package decodestring

import (
	"strconv"
	"strings"
)

func repeat(n int, s string) string {
	var newStr string
	strSeg := []string{}
	strLen := len(s)
	if strLen > 1 {
		for i := 0; i < len(s); {
			num := []byte{}
			var b byte = s[i]
			if !(b >= '0' && b <= '9') {
				// skip string
				j := i
				for ; i < strLen; i++ {
					b = s[i]
					if b >= '0' && b <= '9' {
						break
					}
				}
				strSeg = append(strSeg, s[j:i])
			} else {
				for ; i < strLen; i++ {
					b = s[i]
					if b >= '0' && b <= '9' {
						num = append(num, b)
					} else {
						break
					}
				}
				newN, _ := strconv.ParseInt(string(num), 10, 64)
				i++ // skip [
				j := i
				//find ]
				skipPre := 0
				for ; i < strLen; i++ {
					b = s[i]
					if b == '[' {
						skipPre++
					}
					if b == ']' {
						if skipPre > 0 {
							skipPre--
						} else {
							break
						}
					}
				}
				expanded := repeat(int(newN), s[j:i])
				strSeg = append(strSeg, expanded)
				i++
			}
		}
		newStr = strings.Join(strSeg, "")
	} else {
		newStr = s
	}
	if n == 1 {
		return newStr
	}
	ret := make([]string, n)
	for i := 0; i < n; i++ {
		ret = append(ret, newStr)
	}
	return strings.Join(ret, "")
}
func decodeString(s string) string {
	return repeat(1, s)
}
