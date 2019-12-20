package main

import (
	"fmt"
)

func main() {

	var (
		n   int
		x   int
		sum int
	)

	fmt.Printf("n: ")
	fmt.Scanf("%d", &n)

	for i := 0; i < int(n); i++ {
		fmt.Print("x: ")
		fmt.Scanf("%d", &x)
		sum += int(x)

	}
	fmt.Println("", sum)

}
