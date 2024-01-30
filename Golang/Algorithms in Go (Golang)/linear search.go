package main
import (
	"fmt"
)
// linearSearch function returns the index of the element if found, else returns -1
func linearSearch(arr []int, x int) int {
	for i, item := range arr {
		if item == x {
			return i
		}
	}
	return -1
}
func main() {
	data := []int{20, 40, 80, 60, 10}
	searchNum := 60
	index := linearSearch(data, searchNum)
	if index != -1 {
		fmt.Printf("Element %d is present at index %d.\n", searchNum, index)
	} else {
		fmt.Printf("Element %d is not present in the array.\n", searchNum)
	}
}