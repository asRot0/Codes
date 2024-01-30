package main
import (
	"fmt"
)
type Node struct {
	data int
	next *Node
	prev *Node
}
type DoublyLinkedList struct {
	head *Node
	tail *Node
}
func (list *DoublyLinkedList) Append(data int) {
	newNode := &Node{data: data}
	if list.head == nil {
		list.head = newNode
		list.tail = newNode
		return
	}
	newNode.prev = list.tail
	list.tail.next = newNode
	list.tail = newNode
}
func (list *DoublyLinkedList) DeleteWithValue(data int) {
	current := list.head
	for current != nil {
		if current.data == data {
			if current.prev != nil {
				current.prev.next = current.next
			} else {
				list.head = current.next
			}
			if current.next != nil {
				current.next.prev = current.prev
			} else {
				list.tail = current.prev
			}
			return
		}
		current = current.next
	}
}
func (list *DoublyLinkedList) Display() {
	current := list.head
	for current != nil {
		fmt.Print(current.data, " <-> ")
		current = current.next
	}
	fmt.Println("nil")
}
func main() {
	list := &DoublyLinkedList{}
	list.Append(1)
	list.Append(2)
	list.Append(3)
	list.Display()
	list.DeleteWithValue(2)
	list.Display()
}