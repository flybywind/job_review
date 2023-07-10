package main

import (
	"fmt"
	"time"
)

func func1(n int, ch chan int) {
	//sending into the channel
	time.Sleep(time.Second * 2)
	ch <- n
	fmt.Println("send value")
}

func main() {
	// declaring a bidirectional channel that transports data of type int
	c := make(chan int)
	fmt.Printf("%T\n", c)

	// starting the goroutine
	go func1(10, c)

	fmt.Println("waiting Value ...")
	//waiting the send value arriving,
	// receiving data from the channel
	n := <-c
	fmt.Println("Value received:", n)

	fmt.Println("Exiting main ...")
}
