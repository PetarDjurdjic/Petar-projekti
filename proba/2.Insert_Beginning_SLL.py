class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertHead(self, newNode):
        if self.head is None:
            self.head = newNode
        newNode.next = self.head
        self.head = newNode

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.value)
            currentNode = currentNode.next


firstNode = Node("John")
linkedList = LinkedList()
linkedList.insertEnd(firstNode)
secondNode = Node("Ben")
linkedList.insertEnd(secondNode)
thirdNode = Node("Matthew")
linkedList.insertHead(thirdNode)
linkedList.printList()

