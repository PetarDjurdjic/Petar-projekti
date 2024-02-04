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


    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head

    def find_middle(self):
        if self.length % 2 == 1:
            prev_node = self.head
            for _ in range((self.length - 1) // 2):
                prev_node = prev_node.next
            return prev_node.value
        else:
            prev_node = self.head
            for _ in range(self.length // 2):
                prev_node = prev_node.next
            return prev_node.value


new_linked_list = LinkedList(78)
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(50)
print(new_linked_list)
# print(new_lin ked_list.remove(3))
# print(new_linked_list)
print(new_linked_list.reverse())
print(new_linked_list)
print(new_linked_list.find_middle())
new_linked_list.find_middle()
