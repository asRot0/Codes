package main
import (
	"fmt"
)
// binarySearch function returns the index of the element if found, else returns -1
func binarySearch(arr []int, l int, r int, x int) int {
	if r >= l {
		mid := l + (r-l)/2
		// If the element is present at the middle itself
		if arr[mid] == x {
			return mid
		}
		// If the element is smaller than mid, search in the left sub-array
		if arr[mid] > x {
			return binarySearch(arr, l, mid-1, x)
		}
		// Else, search in the right sub-array
		return binarySearch(arr, mid+1, r, x)
	}
	// If the element is not present in the array
	return -1
}
func main() {
	data := []int{10, 20, 30, 40, 50, 60, 70, 80, 90}
	searchNum := 70
	index := binarySearch(data, 0, len(data)-1, searchNum)
	if index != -1 {
		fmt.Printf("Element %d is present at index %d.\n", searchNum, index)
	} else {
		fmt.Printf("Element %d is not present in the array.\n", searchNum)
	}
}