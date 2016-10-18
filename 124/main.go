package main

import (
	"fmt"
	"math"
	"sort"
)

func intInArray(n int, list []int) bool {
	for _, x := range list {
		if n == x {
			return true
		}
	}
	return false
}

func uniquePrimeFactors(n int) []int {
	prime_factors := make([]int, 0, 8);
	i := 2

	for i < int(math.Ceil(math.Sqrt(float64(n)))) + 1 {
		for math.Mod(float64(n), float64(i)) == 0 {

			if !intInArray(i, prime_factors) {
				prime_factors = append(prime_factors, i)
			}
			n /= i
		}
		i++
	}

	// add last n
	prime_factors = append(prime_factors, n)

	return prime_factors;
}

func rad(n int) int {
	s := 1
	for _, x := range uniquePrimeFactors(n) {
		s *= x
	}
	return s
}

func main() {

	max := 10
	rad_list := make([]int, 0, max)
	for i := 1; i <= max; i++ {
		pf := rad(i)
		rad_list = append(rad_list, pf)
		fmt.Println(i, pf)
	}
	sort.Ints(rad_list)
	fmt.Println(rad_list)
	fmt.Println("done")
}
