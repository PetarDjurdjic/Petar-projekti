class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
        # return f"{self.prev}<-{self.value}->{self.next}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += "<->"
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1

    def prepend(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next


newDll = DoublyLinkedList()
newDll.append(10)
newDll.append(20)
newDll.append(30)
newDll.prepend(50)
print(newDll)
newDll.traverse()
