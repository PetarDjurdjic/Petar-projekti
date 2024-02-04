class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList:
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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

    # def remove(self, index):
    #     if index < 0 or index >= self.length:
    #         return None
    #     elif index == 0:
    #         removed_node = self.head
    #         if self.length == 1:
    #             self.head = None
    #             self.tail = None
    #         else:
    #             self.head = self.head.next
    #         removed_node.next = None
    #         self.length -=1
    #
    #     else:
    #         prev_node = self.head
    #         for _ in range(index - 1):
    #             prev_node = prev_node.next
    #         removed_node = prev_node.next
    #         prev_node.next = removed_node.next
    #         removed_node.next = None
    #     self.length -= 1
    #     return removed_node


    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        # if node to be removed is the head node
        elif index == 0:
            popped_node = self.head
            if self.length == 0:
                self.head = None
                self.tail = None
            else:
                self.head = popped_node.next
            popped_node.next = None
            self.length -=1
            return popped_node

        else:
            prev_node = self.head
            for _ in range(index-1):
                prev_node = prev_node.next
            popped_node = prev_node.next

            # if node to be removed is the tail node
            if popped_node.next is None:
                self.tail = prev_node

            prev_node.next = prev_node.next.next
            popped_node.next = None
            self.length -=1
            return popped_node







new_linked_list = LinkedList(78)
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
print(new_linked_list)
print(new_linked_list.remove(3))
print(new_linked_list)

