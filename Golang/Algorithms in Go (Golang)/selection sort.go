package main
import (
	"fmt"
)
func SelectionSort(arr []int) {
	n := len(arr)
	for i := 0; i < n-1; i++ {
		minIdx := i
		for j := i + 1; j < n; j++ {
			if arr[j] < arr[minIdx] {
				minIdx = j
			}
		}
		// Swap the found minimum element with the first element
		arr[i], arr[minIdx] = arr[minIdx], arr[i]
	}
}
func main() {
	data := []int{64, 34, 25, 12, 22, 11, 90}
	fmt.Println("Original array:", data)
	SelectionSort(data)
	fmt.Println("Sorted array:  ", data)
}