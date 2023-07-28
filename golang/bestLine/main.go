package bestline

import (
	"math"
)

type point struct {
	x, y int
}
type line struct {
	p1, p2  int
	points  map[point]struct{}
	a, b, c float32 // line attribute, a*x + b*y = c
}

func floatEqal(a, b float32, eps float32) bool {
	d := a - b
	if d < 0 {
		d = -d
	}
	return d < eps
}
func (l line) lieAt(p point) bool {
	return floatEqal(l.a*float32(p.x)+l.b*float32(p.y), l.c, 1e-2)
}

func from2point(p1, p2 point) *line {
	x1, y1 := p1.x, p1.y
	x2, y2 := p2.x, p2.y
	l := &line{
		p1:     math.MaxInt,
		p2:     math.MaxInt,
		points: map[point]struct{}{},
	}
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

func (l *line) addPoint(idx int, ps pointSlice) {
	p := ps[idx]
	// idx = p.oriIdx
	l.points[p] = struct{}{}
	if idx < l.p1 {
		l.p2 = l.p1
		l.p1 = idx
	} else if idx < l.p2 {
		l.p2 = idx
	}
}

type pointSlice []point

func bestLine(points [][]int) []int {
	pointNum := len(points)
	ps := make(pointSlice, pointNum)
	for i, p := range points {
		ps[i] = point{p[0], p[1]}
	}
	lineMap := map[[2]int]*line{} // key: index in points
	maxPiontInLine := 0
	retIndx := []int{0, 0}
	for i := 0; i < pointNum; i++ {
		p1 := ps[i]
		pointMap := map[int]struct{}{} // local map, storing the points that have already been verified in one line
		pointMap[i] = struct{}{}
		for j := i + 1; j < pointNum; j++ {
			p2 := ps[j]
			if _, ok := pointMap[j]; !ok {
				pointMap[j] = struct{}{}
				newLine := from2point(p1, p2)
				lineMap[[2]int{i, j}] = newLine
				newLine.addPoint(i, ps)
				newLine.addPoint(j, ps)
				for k := 0; k < pointNum; k++ {
					if _, ok := pointMap[k]; ok {
						continue
					}
					if newLine.lieAt(ps[k]) {
						pointMap[k] = struct{}{}
						newLine.addPoint(k, ps)
						lineMap[[2]int{i, k}] = newLine
						lineMap[[2]int{j, k}] = newLine
					}
				}
				if len(newLine.points) > maxPiontInLine {
					maxPiontInLine = len(newLine.points)
					retIndx[0] = newLine.p1
					retIndx[1] = newLine.p2
				}
			}

		}
	}
	return retIndx
}
