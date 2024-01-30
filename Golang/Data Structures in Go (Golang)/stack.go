package main
import (
	"fmt"
	"errors"
)
type Stack []int
func (s *Stack) Push(v int) {
	*s = append(*s, v)
}
func (s *Stack) Pop() (int, error) {
	if len(*s) == 0 {
		return 0, errors.New("Stack is empty")
	}
	res := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]
	return res, nil
}
func (s *Stack) Peek() (int, error) {
	if len(*s) == 0 {
		return 0, errors.New("Stack is empty")
	}
	return (*s)[len(*s)-1], nil
}
func (s *Stack) IsEmpty() bool {
	return len(*s) == 0
}
func main() {
	var stack Stack
	stack.Push(5)
	stack.Push(10)
	stack.Push(15)
	fmt.Println("Top of the Stack:", stack.Peek())
	fmt.Println("Stack:", stack)
	popped, _ := stack.Pop()
	fmt.Println("Popped:", popped)
	fmt.Println("Stack after Pop:", stack)
}