package bestline

import (
	"fmt"
	"math"
	"os"
	"runtime/pprof"
)

type point struct {
	x, y int
}
type line struct {
	p1, p2  int
	points  int
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
	return floatEqal(l.a*float32(p.x)+l.b*float32(p.y), l.c, 0.1)
}

func from2point(p1, p2 point) *line {
	x1, y1 := p1.x, p1.y
	x2, y2 := p2.x, p2.y
	l := &line{
		p1:     math.MaxInt,
		p2:     math.MaxInt,
		points: 0,
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

func (l *line) addPoint(idx int) {
	l.points++
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
		for j := i + 1; j < pointNum; j++ {
			p2 := ps[j]

			_, k1 := lineMap[[2]int{i, j}]
			_, k2 := lineMap[[2]int{j, i}]
			if k1 || k2 {
				continue
			}
			newLine := from2point(p1, p2)
			newLine.addPoint(i)
			newLine.addPoint(j)
			lineMap[[2]int{i, j}] = newLine
			// todo check if (i, j) hit lineMap
			for k := 0; k < pointNum; k++ {
				// add other points that lie at line comprised of [i,j]
				if k == i || k == j {
					continue
				}
				if newLine.lieAt(ps[k]) {
					newLine.addPoint(k)
					lineMap[[2]int{i, k}] = newLine
					lineMap[[2]int{j, k}] = newLine
				}
			}
			if newLine.points > maxPiontInLine {
				maxPiontInLine = newLine.points
				retIndx[0] = newLine.p1
				retIndx[1] = newLine.p2
			}

		}
	}
	return retIndx
}

func Pprof() {
	f, err := os.Create("bestline.prof")
	if err != nil {
		panic(err)
	}
	defer f.Close()

	// Start CPU profiling
	if err := pprof.StartCPUProfile(f); err != nil {
		panic(err)
	}
	var res, res2 []int
	for n := 0; n < 100; n++ {
		res = bestLine([][]int{{-24272, -29606}, {-37644, -4251}, {2691, -22513}, {-14592, -33765}, {-21858, 28550}, {-22264, 41303}, {-6960, 12785}, {-39133, -41833}, {25151, -26643}, {-19416, 28550}, {-17420, 22270}, {-8793, 16457}, {-4303, -25680}, {-14405, 26607}, {-49083, -26336}, {22629, 20544}, {-23939, -25038}, {-40441, -26962}, {-29484, -30503}, {-32927, -18287}, {-13312, -22513}, {15026, 12965}, {-16361, -23282}, {7296, -15750}, {-11690, -21723}, {-34850, -25928}, {-14933, -16169}, {23459, -9358}, {-45719, -13202}, {-26868, 28550}, {4627, 16457}, {-7296, -27760}, {-32230, 8174}, {-28233, -8627}, {-26520, 28550}, {5515, -26001}, {-16766, 28550}, {21888, -3740}, {1251, 28550}, {15333, -26322}, {-27677, -19790}, {20311, 7075}, {-10751, 16457}, {-47762, -44638}, {20991, 24942}, {-19056, -11105}, {-26639, 28550}, {-19862, 16457}, {-27506, -4251}, {-20172, -5440}, {-33757, -24717}, {-9411, -17379}, {12493, 29906}, {0, -21755}, {-36885, -16192}, {-38195, -40088}, {-40079, 7667}, {-29294, -34032}, {-55968, 23947}, {-22724, -22513}, {20362, -11530}, {-11817, -23957}, {-33742, 5259}, {-10350, -4251}, {-11690, -22513}, {-20241, -22513}})
		res2 = bestLine([][]int{{-13260, 8589}, {1350, 8721}, {-37222, -19547}, {-54293, -29302}, {-10489, -13241}, {-19382, 574}, {5561, 1033}, {-22508, -13241}, {-1542, 20695}, {9277, 2820}, {-32081, 16145}, {-50902, 23701}, {-8636, 19504}, {-17042, -28765}, {-27132, -24156}, {-48323, -4607}, {30279, 29922}})
	}
	pprof.StopCPUProfile()
	fmt.Printf("res = %v, %v\n", res, res2)
}
