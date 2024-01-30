package main

import "fmt"

func main() {
    sample := [3][3]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}

    //Print array element
   fmt.Println("Access an array by index:")
    fmt.Println(sample[0][0])
    fmt.Println(sample[0][1])
    fmt.Println(sample[0][2])
    fmt.Println(sample[1][0])
    fmt.Println(sample[1][1])
    fmt.Println(sample[1][2])
    fmt.Println(sample[2][0])
    fmt.Println(sample[2][1])
    fmt.Println(sample[2][2])

    // loop array using for-range
    fmt.Println("Using for-range")
    for _, row := range sample {
        for _, val := range row {
            fmt.Println(val)
        }
    }

    // loop array using for loop
    fmt.Println("\nUsing for loop")
    for i := 0; i < len(sample); i++ {
        for j := 0; j < 3; j++ {
            fmt.Println(sample[i][j])
        }
    }

    fmt.Println("\nUsing for loop - Second way")
    for i := 0; i < len(sample); i++ {
        for j := 0; j < len(sample[i]); j++ {
            fmt.Println(sample[i][j])
        }
    }

    //Assign new values
     fmt.Println("Assign new values")
    sample[0][0] = 9
    sample[0][1] = 8
    sample[0][2] = 7
    sample[1][0] = 6
    sample[1][1] = 5
    sample[1][2] = 4
    sample[2][0] = 3
    sample[2][1] = 2
    sample[2][2] = 1

    fmt.Println("Access an new values from array by index:")
    fmt.Println(sample[0][0])
    fmt.Println(sample[0][1])
    fmt.Println(sample[0][2])
    fmt.Println(sample[1][0])
    fmt.Println(sample[1][1])
    fmt.Println(sample[1][2])
    fmt.Println(sample[2][0])
    fmt.Println(sample[2][1])
    fmt.Println(sample[2][2])
}