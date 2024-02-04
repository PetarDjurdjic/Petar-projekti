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


    def mergeLists(firstList, secondList, mergedList):
        currentFirst = firstList.head
        currentSecond = secondList.head
        while True:
            if currentFirst is None:
                mergedList.insertEnd(currentSecond)
                break
            if currentSecond is None:
                mergedList.insertEnd(currentFirst)
                break
            if currentFirst == currentSecond:
                currentFirst_next = currentFirst.next
                currentFirst.next = None
                mergedList.insertEnd(currentFirst)
                currentFirst = currentFirst_next
                currentSecond_next = currentSecond.next
                currentSecond.next = None
                mergedList.insertEnd(currentSecond)
                currentSecond = currentSecond_next

            if currentFirst.value < currentSecond.value:
                currentFirst_next = currentFirst.next
                currentFirst.next = None
                mergedList.insertEnd(currentFirst)
                currentFirst = currentFirst_next

            else:
                currentSecond_next = currentSecond.next
                currentSecond.next = None
                mergedList.insertEnd(currentSecond)
                currentSecond = currentSecond_next

nodeOne = Node(1)
nodeTwo = Node(3)
nodeThree = Node(4)
firstList = LinkedList()
firstList.insertEnd(nodeOne)
firstList.insertEnd(nodeTwo)
firstList.insertEnd(nodeThree)

nodeFour = Node(1)
nodeFive = Node(2)
nodeSix = Node(9)
secondList = LinkedList()
secondList.insertEnd(nodeFour)
secondList.insertEnd(nodeFive)
secondList.insertEnd(nodeSix)

print("Printing first list:")
firstList.printList()
print("Printing second list:")
secondList.printList()


mergedList = LinkedList()
LinkedList.mergeLists(firstList, secondList, mergedList)
print("Printing merged lists")
mergedList.printList()

