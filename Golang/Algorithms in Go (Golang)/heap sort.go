package main
import (
	"fmt"
)
func heapify(arr []int, n, i int) {
	largest := i          // Initialize largest as root
	l := 2*i + 1          // left child index
	r := 2*i + 2          // right child index
	// Check if left child exists and is greater than root
	if l < n && arr[l] > arr[largest] {
		largest = l
	}
	// Check if right child exists and is greater than largest
	if r < n && arr[r] > arr[largest] {
		largest = r
	}
	// If the largest isn't root
	if largest != i {
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, n, largest)
	}
}
func heapSort(arr []int) {
	n := len(arr)
	// Build a max heap
	for i := n/2 - 1; i >= 0; i-- {
		heapify(arr, n, i)
	}
	// Extract elements from heap one by one
	for i := n - 1; i >= 0; i-- {
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr, i, 0)
	}
}
func main() {
	data := []int{12, 11, 13, 5, 6, 7}
	fmt.Println("Original array:", data)
	heapSort(data)
	fmt.Println("Sorted array:  ", data)
}