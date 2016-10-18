package main

import (
	"fmt"
	"math"
)

func primeFactors(n int) []int {
	prime_factors := make([]int, 0, 8);
	prime_factors = append(prime_factors, 1)
	i := float64(n) / 2
	i = math.Floor(i)

	for n != 1 && i > 0 {
		r := math.Mod(float64(n), float64(i))
		if r == 0 {
			n = int(float64(n) / i)
			prime_factors = append(prime_factors, int(i))
		} else {
			i--
		}
	}
	return prime_factors;
}

func main() {
	for i := 11; i < 10000; i++ {
		pf := primeFactors(i)
		fmt.Println(i, pf)
	}
}
