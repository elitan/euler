package main

import (
	"fmt"
	"math"
	"os"
)
func main() {

	var i uintptr = 1000000000000
	var x uintptr = 0
	var x2 float64 = 0
	var y float64
	var balls float64

	for {
		x = i * (i - 1)
		x2 = float64(x * 2)
		y = math.Ceil(math.Sqrt(x2)) * math.Floor(math.Sqrt(x2))

		if int(x2) == int(y) {

			fmt.Println("x2 == y")
			fmt.Println(i, int(y))
			fmt.Println("balls: ", int(balls))

			fmt.Println(int(math.Ceil(math.Sqrt(x2))))

			os.Exit(1)
		}
		i++
	}


}
