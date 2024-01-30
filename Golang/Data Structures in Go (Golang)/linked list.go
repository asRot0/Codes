package main
import (
	"fmt"
)
type Node struct {
	data int
	next *Node
}
type LinkedList struct {
	head *Node
}
func (list *LinkedList) Append(data int) {
	newNode := &Node{data: data}
	if list.head == nil {
		list.head = newNode
		return
	}
	current := list.head
	for current.next != nil {
		current = current.next
	}
	current.next = newNode
}
func (list *LinkedList) DeleteWithValue(data int) {
	if list.head == nil {
		return
	}
	if list.head.data == data {
		list.head = list.head.next
		return
	}
	current := list.head
	for current.next != nil && current.next.data != data {
		current = current.next
	}
	if current.next != nil {
		current.next = current.next.next
	}
}
func (list *LinkedList) Display() {
	current := list.head
	for current != nil {
		fmt.Print(current.data, " -> ")
		current = current.next
	}
	fmt.Println("nil")
}
func main() {
	list := &LinkedList{}
	list.Append(1)
	list.Append(2)
	list.Append(3)
	list.Display()
	list.DeleteWithValue(2)
	list.Display()
}