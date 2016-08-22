package main

import (
    "fmt"
)

func main() {
    a := 1
    b := 2
    sum_even := 0

    for b < 4000000 {
        if b % 2 == 0 {
            sum_even += b
        }

        a, b = b, b+a
    }
    fmt.Println(sum_even)
}
