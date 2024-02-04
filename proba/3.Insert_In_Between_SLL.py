class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length +=1
            currentNode = currentNode.next


    def insertHead(self, newNode):
        if self.head is None:
            self.head = newNode
        newNode.next = self.head
        self.head = newNode

    def insertAt(self, newNode, position):
        if position < 0 or position > self.listLength():
            print("Invalid position")
            return
        if position == 0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

        # prev_node = self.head
        # for _ in range(position -1):
        #     prev_node = prev_node.next
        # newNode.next = prev_node.next
        # prev_node.next = newNode

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


firstNode = Node(10)
linkedList = LinkedList()
linkedList.insertEnd(firstNode)
secondNode = Node(20)
linkedList.insertEnd(secondNode)
# linkedList.printList()
thirdNode = Node(15)
linkedList.insertAt(thirdNode, 0 )
linkedList.printList()


