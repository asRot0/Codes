func minPairSum(nums []int) int {
    sort.Ints(nums)
    l, r := 0, len(nums)-1
    maxsum := 0

    for l < r {
        maxsum = max(maxsum, nums[l]+nums[r])
        l++
        r--
    }
    return maxsum
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}