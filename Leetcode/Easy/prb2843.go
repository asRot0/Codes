func countSymmetricIntegers(low int, high int) int {
    res := 0
    for i:= low; i <= high; i++{
        s := strconv.Itoa(i)
        l := len(s)
        leftsum, rightsum := 0, 0
        if l%2 != 0 {
            continue
        }
        for j:=0; j<l/2; j++ {
            leftsum += int(s[j] - '0')
            rightsum += int(s[l-j-1] - '0')
        }
        if leftsum == rightsum {
            res++
        }
    }
    return res
}