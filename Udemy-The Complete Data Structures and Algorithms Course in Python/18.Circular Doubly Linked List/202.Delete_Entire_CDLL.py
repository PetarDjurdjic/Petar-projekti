class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    # Creation of Circular Doubly Linked List
    def createCDLL(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "The CDLL is created successfully."

    # Insertion Method in Circular Doubly Linked List

    def insertCDLL(self, value, location):
        if self.head is None:
            return "The CDLL does not exist."
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index +=1
                newNode.next = temp_node.next
                newNode.prev = temp_node
                temp_node.next.prev = newNode
                temp_node.next = newNode
        return "The node has been successfully inserted."

    # Traversal of Circular Doubly Linked List
    def traversalCDLL(self):
        if self.head is None:
            print("There is not any node for traversal.")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next


    # Reverse traversal of Circular Doubly Linked List

    def reverseTraversalCDLL(self):
        if self.head is None:
            print("There is not any node for reverse traversal.")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    # Search Circular Doubly Linked List
    def searchCDLL(self,nodeValue):
        if self.head is None:
            print("There is not any node in circular doubly linked list.")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                if tempNode == self.tail:
                    return "The value does not exist in CDLL."
                tempNode = tempNode.next

    # Delete a node from CDLL

    def deleteNode(self, location):
        if self.head is None:
            print("There is not any node to delete.")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index +=1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode
            print("The node has been successfully deleted.")

    # Delete entire CDLL
    def deleteCDLL(self):
        if self.head is None:
            print("There is not any element to delete.")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The CDLL has been successfully deleted.")

circularDLL = CircularDoublyLinkedList()
print(circularDLL.createCDLL(5))
circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(1,1)
circularDLL.insertCDLL(2,2)
circularDLL.insertCDLL(9,0)

print([node.value for node in circularDLL])
circularDLL.deleteCDLL()
print([node.value for node in circularDLL])
