package main
import (
	"errors"
	"fmt"
	"sort"
)
type Item struct {
	value    string
	priority int
}
type PriorityQueue []*Item
func (pq *PriorityQueue) Enqueue(value string, priority int) {
	item := &Item{
		value:    value,
		priority: priority,
	}
	*pq = append(*pq, item)
	sort.SliceStable(*pq, func(i, j int) bool {
		return (*pq)[i].priority > (*pq)[j].priority
	})
}
func (pq *PriorityQueue) Dequeue() (string, error) {
	if len(*pq) == 0 {
		return "", errors.New("PriorityQueue is empty")
	}
	item := (*pq)[0]
	*pq = (*pq)[1:]
	return item.value, nil
}
func (pq *PriorityQueue) Peek() (string, error) {
	if len(*pq) == 0 {
		return "", errors.New("PriorityQueue is empty")
	}
	item := (*pq)[0]
	return item.value, nil
}
func main() {
	var pq PriorityQueue
	pq.Enqueue("Task 1", 2)
	pq.Enqueue("Task 2", 1)
	pq.Enqueue("Task 3", 3)
	fmt.Println("Peek at top priority item:", pq.Peek())
	deq, _ := pq.Dequeue()
	fmt.Println("Dequeued:", deq)
}