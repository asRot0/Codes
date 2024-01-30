package main
import (
	"fmt"
)
func BubbleSort(arr []int) {
	n := len(arr)
	for i := 0; i < n-1; i++ {
		swapped := false
		for j := 0; j < n-i-1; j++ {
			if arr[j] > arr[j+1] {
				// swap arr[j] and arr[j+1]
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = true
			}
		}
		// If no two elements were swapped by the inner loop, then the array is sorted
		if !swapped {
			break
		}
	}
}
func main() {
	data := []int{64, 34, 25, 12, 22, 11, 90}
	fmt.Println("Original array:", data)
	BubbleSort(data)
	fmt.Println("Sorted array:  ", data)
}