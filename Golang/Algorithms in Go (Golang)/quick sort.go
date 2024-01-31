package main
import (
	"fmt"
)
// partition rearranges the elements by partitioning around the pivot
func partition(arr []int, low, high int) int {
	pivot := arr[high]  // choosing last element as pivot
	i := low - 1        // index of smaller element
	for j := low; j < high; j++ {
		if arr[j] < pivot {
			i++
			arr[i], arr[j] = arr[j], arr[i]  // swap
		}
	}
	arr[i+1], arr[high] = arr[high], arr[i+1]  // swap pivot into its correct position
	return i + 1
}
// QuickSort sorts the array using quick sort algorithm
func QuickSort(arr []int, low, high int) {
	if low < high {
		pi := partition(arr, low, high)  // pi is partitioning index
		QuickSort(arr, low, pi-1)  // sort elements before partition
		QuickSort(arr, pi+1, high) // sort elements after partition
	}
}
func main() {
	data := []int{10, 80, 30, 90, 40, 50, 70}
	fmt.Println("Original array:", data)
	QuickSort(data, 0, len(data)-1)
	fmt.Println("Sorted array:  ", data)
}