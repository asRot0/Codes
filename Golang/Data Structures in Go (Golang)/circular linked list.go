package main
import (
	"fmt"
)
type Node struct {
	data int
	next *Node
}
type CircularLinkedList struct {
	head *Node
}
func (list *CircularLinkedList) Append(data int) {
	newNode := &Node{data: data}
	if list.head == nil {
		list.head = newNode
		newNode.next = list.head
		return
	}
	temp := list.head
	for temp.next != list.head {
		temp = temp.next
	}
	temp.next = newNode
	newNode.next = list.head
}
func (list *CircularLinkedList) DeleteWithValue(data int) {
	if list.head == nil {
		return
	}
	if list.head.data == data {
		curr := list.head
		for curr.next != list.head {
			curr = curr.next
		}
		if list.head.next == list.head { // Only one node
			list.head = nil
		} else {
			curr.next = list.head.next
			list.head = list.head.next
		}
		return
	}
	curr := list.head
	for curr.next != list.head && curr.next.data != data {
		curr = curr.next
	}
	if curr.next.data == data {
		curr.next = curr.next.next
	}
}
func (list *CircularLinkedList) Display() {
	if list.head == nil {
		fmt.Println("List is empty")
		return
	}
	temp := list.head
	for {
		fmt.Print(temp.data, " -> ")
		temp = temp.next
		if temp == list.head {
			break
		}
	}
	fmt.Println(list.head.data)
}
func main() {
	list := &CircularLinkedList{}
	list.Append(1)
	list.Append(2)
	list.Append(3)
	list.Display()
	list.DeleteWithValue(2)
	list.Display()
}