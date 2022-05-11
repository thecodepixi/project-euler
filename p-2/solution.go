package main

import "fmt"

func fibTotal(max int) int {
	var a, b int = 0, 1
	var total int = 0

	for a < max {
		if a % 2 == 0 {
			total += a
		}
		a, b = b, a + b
	}

	return total
}

func main() {
	fmt.Println( fibTotal(4_000_000) )
}