package main
import (
	"fmt"
)
type Node struct {
	data  int
	left  *Node
	right *Node
}
// Insert a value into the BST
func (n *Node) Insert(value int) {
	if value <= n.data {
		if n.left == nil {
			n.left = &Node{data: value}
		} else {
			n.left.Insert(value)
		}
	} else {
		if n.right == nil {
			n.right = &Node{data: value}
		} else {
			n.right.Insert(value)
		}
	}
}
// Search for a value in the BST
func (n *Node) Search(value int) bool {
	if n == nil {
		return false
	}
	if value == n.data {
		return true
	}
	if value < n.data {
		return n.left.Search(value)
	}
	return n.right.Search(value)
}
// InOrder traversal of the BST
func (n *Node) InOrder() {
	if n != nil {
		n.left.InOrder()
		fmt.Print(n.data, " ")
		n.right.InOrder()
	}
}
func main() {
	root := &Node{data: 50}
	root.Insert(30)
	root.Insert(70)
	root.Insert(20)
	root.Insert(40)
	root.Insert(60)
	root.Insert(80)
	fmt.Print("InOrder Traversal: ")
	root.InOrder()
	fmt.Println("\nSearch for 25:", root.Search(25))
	fmt.Println("Search for 60:", root.Search(60))
}