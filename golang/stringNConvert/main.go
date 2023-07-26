package stringnconvert

import "strings"

var dir2 = [2][2]int{{0, 1}, {1, -1}}

type Compare func(int) bool
type collision struct {
	bound int
	cmp   Compare
}

func convert(s string, numRows int) string {
	if numRows == 1 {
		return s
	}
	collCond := []*collision{
		{
			bound: numRows,
			cmp: func(p int) bool {
				// bigger than numRows
				return p >= numRows
			},
		},
		{
			bound: -1,
			cmp: func(p int) bool {
				// bigger than -1
				return p <= -1
			},
		},
	}
	bufMat := make([][]string, numRows)
	totalChar := len(s)
	colN := (totalChar/(2*numRows-2) + 1) * (numRows - 1)
	for i := 0; i < numRows; i++ {
		bufMat[i] = make([]string, colN)
	}
	x, y := 0, 0
	d := 0
	for i := 0; i < totalChar; {
		cond := collCond[d]
		if cond.cmp(y) {
			// collide
			x, y = x-dir2[d][0], y-dir2[d][1]
			d++
			d = d % 2
		} else {
			bufMat[y][x] = s[i : i+1]
			i++
		}
		x, y = x+dir2[d][0], y+dir2[d][1]
	}
	ret := make([]string, 0, totalChar)
	for y := 0; y < numRows; y++ {
		for x := 0; x < colN; x++ {
			if len(bufMat[y][x]) > 0 {
				ret = append(ret, bufMat[y][x])
			}
		}
	}
	return strings.Join(ret, "")
}

/** Python :
简单的过程模拟当然可以解决问题，但是如果换个思路，其实可能找到更优的模拟方法
*/
// class Solution:
//     def convert(self, s: str, numRows: int) -> str:
//         if numRows < 2: return s
//         res = ["" for _ in range(numRows)]
//         i, flag = 0, -1
//         for c in s:
//             res[i] += c
//             if i == 0 or i == numRows - 1: flag = -flag
//             i += flag
//         return "".join(res)

// 作者：jyd
// 链接：https://leetcode.cn/problems/zigzag-conversion/solution/zzi-xing-bian-huan-by-jyd/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
