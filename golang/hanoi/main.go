package main

import "fmt"

var step int = 0

func Hanoi(n int, from, to, interm int, poles [][]int) {
	if n == 1 {
		fromLen := len(poles[from])
		poles[to] = append(poles[to], poles[from][fromLen-1])
		poles[from] = poles[from][:(fromLen - 1)]
		step++
		fmt.Printf("step%d: from: %d, to: %d \n", step, from+1, to+1)
		fmt.Printf("pole1: %v\n", poles[0])
		fmt.Printf("pole2: %v\n", poles[1])
		fmt.Printf("pole3: %v\n", poles[2])
		fmt.Printf("\n----- ** -----\n")
	} else {
		Hanoi(n-1, from, interm, to, poles)
		Hanoi(1, from, to, interm, poles)
		Hanoi(n-1, interm, to, from, poles)
	}
}

func initHanoiPoles(n int) [][]int {
	ret := make([][]int, 3)
	for i := 0; i < 3; i++ {
		ret[i] = make([]int, 0, n)
	}
	for i := 0; i < n; i++ {
		ret[0] = append(ret[0], n-i)
	}
	return ret
}
func main() {
	N := 6
	poles := initHanoiPoles(N)
	fmt.Printf("Init hanoi towers\n")
	fmt.Printf("pole1: %v\n", poles[0])
	fmt.Printf("pole2: %v\n", poles[1])
	fmt.Printf("pole3: %v\n", poles[2])
	fmt.Printf("\n----- ** -----\n")
	Hanoi(N, 0, 2, 1, poles)

}
