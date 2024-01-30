package main
import (
	"fmt"
	"errors"
)
type Queue []int
func (q *Queue) Enqueue(v int) {
	*q = append(*q, v)
}
func (q *Queue) Dequeue() (int, error) {
	if len(*q) == 0 {
		return 0, errors.New("Queue is empty")
	}
	res := (*q)[0]
	*q = (*q)[1:]
	return res, nil
}
func (q *Queue) Front() (int, error) {
	if len(*q) == 0 {
		return 0, errors.New("Queue is empty")
	}
	return (*q)[0], nil
}
func (q *Queue) IsEmpty() bool {
	return len(*q) == 0
}
func main() {
	var queue Queue
	queue.Enqueue(5)
	queue.Enqueue(10)
	queue.Enqueue(15)
	fmt.Println("Front of the Queue:", queue.Front())
	fmt.Println("Queue:", queue)
	dequeued, _ := queue.Dequeue()
	fmt.Println("Dequeued:", dequeued)
	fmt.Println("Queue after Dequeue:", queue)
}