class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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
print(linkedList)
secondNode = Node("Ben")
thirdNode = Node("Matthew")
linkedList.insertEnd(secondNode)
linkedList.insertEnd(thirdNode)
linkedList.printList()

