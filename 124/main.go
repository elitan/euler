package main

import (
	"fmt"
	"math"
	"sort"
)


type Row struct {
	n, rad int
}

type Rows []Row

func (slice Rows) Len() int {
	return len(slice);
}

func (slice Rows) Less(i, j int) bool {
	return slice[i].rad < slice[j].rad;
}

func (slice Rows) Swap(i, j int) {
	slice[i], slice[j] = slice[j], slice[i];
}

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
	max := 100000
	rad_list := Rows{}
	for i := 1; i <= max; i++ {
		row := Row{i, rad(i)}
		rad_list = append(rad_list, row)
	}

	sort.Sort(rad_list) // sort on rad

	fmt.Println(rad_list[10000].n)
}
