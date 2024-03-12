func balancedStringSplit(s string) int {
    var balance, substr int
    for c := range s {
        if s[c] == 'L' {
            balance++
        } else {
            balance--
        }
        if balance == 0 {
            substr++
        }
    }
    return substr
}