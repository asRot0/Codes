func isHappy(n int) bool {
    check := map[int]bool{n: true}

    for n!=1{
        var sum int
        for n!=0{
            num := n%10
            sum += num * num
            n /= 10
        }
        n = sum
        if check[n]{
            return false
        }
        check[n] = true
    }
    return true
}