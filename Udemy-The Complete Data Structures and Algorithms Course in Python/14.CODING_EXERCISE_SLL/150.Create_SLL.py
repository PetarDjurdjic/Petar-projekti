class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList():
    def __init__(self,value):
        new_node = Node (value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "->"
            temp_node = temp_node.next
        return result


new_linked_list = LinkedList(73)
print(new_linked_list)