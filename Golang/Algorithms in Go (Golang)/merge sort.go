package main
import (
	"fmt"
)
// Merge merges two sorted sub-arrays
func Merge(arr []int, l, m, r int) {
	n1 := m - l + 1
	n2 := r - m
	// Create temp arrays
	L := make([]int, n1)
	R := make([]int, n2)
	// Copy data to temp arrays L[] and R[]
	for i := 0; i < n1; i++ {
		L[i] = arr[l+i]
	}
	for j := 0; j < n2; j++ {
		R[j] = arr[m+1+j]
	}
	// Merge the temp arrays back into arr[l..r]
	i, j, k := 0, 0, l
	for i < n1 && j < n2 {
		if L[i] <= R[j] {
			arr[k] = L[i]
			i++
		} else {
			arr[k] = R[j]
			j++
		}
		k++
	}
	// Copy the remaining elements of L[], if there are any
	for i < n1 {
		arr[k] = L[i]
		i++
		k++
	}
	// Copy the remaining elements of R[], if there are any
	for j < n2 {
		arr[k] = R[j]
		j++
		k++
	}
}
// MergeSort sorts the array using merge sort algorithm
func MergeSort(arr []int, l, r int) {
	if l < r {
		// Find the middle point
		m := l + (r-l)/2
		// Sort first and second halves
		MergeSort(arr, l, m)
		MergeSort(arr, m+1, r)
		Merge(arr, l, m, r)
	}
}
func main() {
	data := []int{38, 27, 43, 3, 9, 82, 10}
	fmt.Println("Original array:", data)
	MergeSort(data, 0, len(data)-1)
	fmt.Println("Sorted array:  ", data)
}