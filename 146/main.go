// This solution will not work.
// We are looking for consecutive primes and this solution does not handle that at all
// alt 1. Check consecutiveness in the strange_prime_sequence-function
package main

import (
	"fmt"
	"math"
)

func intInList(n int, list []int) bool {
	for _, x := range(list) {
		if n == x {
			return true
		}
	}
	return false
}

func isPrime(n int, known_primes []int) bool {

	// quick check
	if intInList(n, known_primes) {
		return true
	}

	// brute force check
	n_float := float64(n)

	if n == 2 || n == 3 {
		return true
	}
	if n < 2 || int(math.Mod(n_float, 2.0)) == 0 {
		return false
	}
	if n < 9 {
		return true
	}
	if math.Mod(n_float, 3.0) == 0 {
		return false
	}

	r := math.Sqrt(n_float)
	f := 5.0
	for f <= r {
		if math.Mod(n_float, f) == 0 {
			return false
		}
		if math.Mod(n_float, (f + 2.0)) == 0 {
			return false
		}
		f += 6.0
	}
	known_primes = append(known_primes, n)
	return true
}

func strange_prime_sequence(n int, known_primes []int) bool {
	n_pow := int(math.Pow(float64(n), 2))
	i_list := []int{1, 3, 7, 9, 13, 27}

	for _, i := range(i_list) {
		if !isPrime(n_pow + i, known_primes) {
			return false
		}
	}
	return true
}

func main() {

	known_primes := make([]int, 0, 1000)
	for i := 0; i < 20; i++ {
		if strange_prime_sequence(i, known_primes) {
			fmt.Println(i, "is strange")
		}
	}

}
