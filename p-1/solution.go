package main

import "fmt"

func multiples(n int) int {
	sum := 0

	for i := n - 1; i > 0; i-- {
		if i % 3 == 0 || i % 5 == 0 {
			sum += i
		}
	}

	return sum
}

func main() {
	fmt.Println(multiples(10))
	fmt.Println(multiples(100))
	fmt.Println(multiples(1000))
}
