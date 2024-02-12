func countGoodTriplets(arr []int, a int, b int, c int) int {
    count := 0
    l := len(arr)

    for i:=0; i<l-2; i++{
        for j:=i+1; j<l-1; j++{
            for k:=j+1; k<l; k++{
				if abs(arr[i]-arr[j]) <= a && abs(arr[j]-arr[k]) <= b && abs(arr[i]-arr[k]) <= c {
					count++
                }
            }
        }
    }
    return count
}
func abs(x int) int {
    if x < 0{
        return -x
    }
    return x
}