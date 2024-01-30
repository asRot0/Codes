package main
import (
	"fmt"
	"math"
)
type Node struct {
	data   int
	height int
	left   *Node
	right  *Node
}
func (n *Node) updateHeight() {
	n.height = 1 + int(math.Max(float64(height(n.left)), float64(height(n.right))))
}
func height(n *Node) int {
	if n == nil {
		return 0
	}
	return n.height
}
func (n *Node) getBalance() int {
	if n == nil {
		return 0
	}
	return height(n.left) - height(n.right)
}
func rightRotate(y *Node) *Node {
	x := y.left
	T3 := x.right
	x.right = y
	y.left = T3
	y.updateHeight()
	x.updateHeight()
	return x
}
func leftRotate(x *Node) *Node {
	y := x.right
	T2 := y.left
	y.left = x
	x.right = T2
	x.updateHeight()
	y.updateHeight()
	return y
}
func (n *Node) Insert(value int) *Node {
	if n == nil {
		return &Node{data: value, height: 1}
	}
	if value < n.data {
		n.left = n.left.Insert(value)
	} else if value > n.data {
		n.right = n.right.Insert(value)
	} else {
		return n
	}
	n.updateHeight()
	balance := n.getBalance()
	if balance > 1 {
		if value < n.left.data {
			return rightRotate(n)
		}
		return leftRotate(n)
	}
	if balance < -1 {
		if value > n.right.data {
			return leftRotate(n)
		}
		return rightRotate(n)
	}
	return n
}
func main() {
	var root *Node
	root = root.Insert(10)
	root = root.Insert(20)
	root = root.Insert(30)
	root = root.Insert(40)
	root = root.Insert(50)
	root = root.Insert(25)
	fmt.Println("Root node:", root.data)
}