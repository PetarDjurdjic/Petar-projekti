class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length +=1
            currentNode = currentNode.next
        return length


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

    def deleteHead(self):
        if self.isListEmpty() is False:
            previousHead = self.head
            self.head = self.head.next
            previousHead.next = None
        else:
            print("Linked list is empty. Delete failed")

    def deleteAt(self, position):
        if position < 0 or position > self.listLength():
            print("Invalid position")
            return
        if self.isListEmpty() is False:
            if position == 0:
                self.deleteHead()
                return 
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                prev_Node.next = currentNode.next
                currentNode.next = None
                break
            prev_Node = currentNode
            currentNode = currentNode.next
            currentPosition +=1




    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            prev_node = lastNode
            lastNode = lastNode.next
        prev_node.next = None

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
thirdNode = Node("Matthew")
linkedList.insertEnd(secondNode)
linkedList.insertEnd(thirdNode)
linkedList.printList()
print()
linkedList.deleteAt(1)
linkedList.printList()



