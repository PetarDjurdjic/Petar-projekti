# class Solution:
#     def deleteDuplicates(self):
#         cur = self.head
#
#         while cur:
#             while cur.next and cur.next.val == cur.val:
#                 cur.next = cur.next.next
#             cur = cur.next
#         return self.head


# General Class applicable for all lists


# General Class applicable for all lists

from random import randint

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self,values=None):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return "->".join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result +=1
            node = node.next
        return result

    def add(self,value):
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail =self.tail.next
        return self.tail

    def generate(self,n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value,max_value))

    def remove_duplicates(self):
        if self.head is None:
            return
        current_node = self.head
        prev_node = None

        while current_node:
            runner = current_node
            while runner.next:
                if runner.next.value == current_node.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            prev_node = current_node
            self.tail = prev_node
            return self.head

customLL = LinkedList()
customLL.generate(5,0,99)
print(customLL)
customLL.remove_duplicates()
print(customLL)