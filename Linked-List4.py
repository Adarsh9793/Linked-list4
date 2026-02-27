# Linked List Implementation with Insertion, Deletion, Middle, and Reverse Methods

from requests import head


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next
        print()  # for newline

    def insertionAtTail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def insertionAtHead(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insertion(self , value , k):
        if k==0:
            self.insertionAtHead(value)
            return
        
        count = 2
        temp = self.head
        while count < k and temp != None:
            count += 1
            temp = temp.next

        if count < k:
            print("k is greater then len")
            return

        rest = temp.next
        temp.next = Node(value)
        temp.next.next = rest

    def deletion(self , k):
        count = 2
        temp = self.head
        while count < k and temp != None:
            count += 1
            temp = temp.next

        if count < k:
            print("k is greater then len")
            return
        
        temp.next = temp.next.next

    def middle(slf):
        slow = slow.next
        fast = fast.next.next

        while fast !=None and fast.next !=None:
            slow = slow.next
            fast = fast.next.next

        return slow
    
    def reverse(slf):
        prev = None
        curr = slf.head

        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        slf.head = prev




# Test
linkedList = LinkedList()
linkedList.insertionAtTail(1)
linkedList.insertionAtTail(2)
linkedList.insertionAtTail(3)
linkedList.insertionAtHead(0)
linkedList.insertion(5,3)
linkedList.printLinkedList()
linkedList.deletion(4)

linkedList.printLinkedList()