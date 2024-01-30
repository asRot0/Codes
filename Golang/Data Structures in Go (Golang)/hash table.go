package main
import (
	"fmt"
	"linkedlist"
)
type KeyValuePair struct {
	Key   string
	Value string
}
type HashTable struct {
	size  int
	table []*linkedlist.LinkedList
}
func NewHashTable(size int) *HashTable {
	return &HashTable{
		size:  size,
		table: make([]*linkedlist.LinkedList, size),
	}
}
func (h *HashTable) hashFunction(key string) int {
	sum := 0
	for _, v := range key {
		sum += int(v)
	}
	return sum % h.size
}
func (h *HashTable) Put(key, value string) {
	index := h.hashFunction(key)
	if h.table[index] == nil {
		h.table[index] = linkedlist.NewLinkedList()
	}
	node := &linkedlist.Node{Value: KeyValuePair{Key: key, Value: value}}
	h.table[index].Append(node)
}
func (h *HashTable) Get(key string) string {
	index := h.hashFunction(key)
	list := h.table[index]
	for node := list.Head; node != nil; node = node.Next {
		if node.Value.(KeyValuePair).Key == key {
			return node.Value.(KeyValuePair).Value
		}
	}
	return ""
}
func (h *HashTable) Delete(key string) {
	index := h.hashFunction(key)
	list := h.table[index]
	for node := list.Head; node != nil; node = node.Next {
		if node.Value.(KeyValuePair).Key == key {
			list.Delete(node)
			return
		}
	}
}
func main() {
	hashTable := NewHashTable(10)
	hashTable.Put("name", "John")
	hashTable.Put("age", "25")
	fmt.Println("Name:", hashTable.Get("name"))
	fmt.Println("Age:", hashTable.Get("age"))
	hashTable.Delete("name")
	fmt.Println("Name after delete:", hashTable.Get("name"))
}