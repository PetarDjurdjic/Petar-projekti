class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += "->"
        return result

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length +=1


    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length +=1

    def insert(self,value, index):
        new_node = Node(value)
        if index > self.length or index < 0:
            raise Exception("Index out of range")
        if index ==0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            prev_node = self.head
            for _ in range(index - 1):
                prev_node = prev_node.next
            new_node.next = prev_node.next
            prev_node.next = new_node
        self.length += 1

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
            if current == self.head:
                break

    def search(self,target):
        current = self.head
        while current is not None:
            if current.value == target:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def get(self,index):
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

cslinkedList = CSLinkedList()
cslinkedList.append(10)
cslinkedList.append(20)
cslinkedList.append(30)
cslinkedList.append(40)
cslinkedList.insert(50, 0)

print(cslinkedList)
print(cslinkedList.get(2))