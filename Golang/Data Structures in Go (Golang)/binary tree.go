package main
import (
	"fmt"
)
type Node struct {
	data  int
	left  *Node
	right *Node
}
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
func (n *Node) InOrder() {
	if n.left != nil {
		n.left.InOrder()
	}
	fmt.Print(n.data, " ")
	if n.right != nil {
		n.right.InOrder()
	}
}
func main() {
	root := &Node{data: 10}
	root.Insert(5)
	root.Insert(15)
	root.Insert(8)
	fmt.Print("InOrder Traversal: ")
	root.InOrder()
}